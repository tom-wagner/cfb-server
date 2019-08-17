from typing import Dict, List, Optional, DefaultDict, Set
from statistics import mean
from collections import Counter, defaultdict
from random import random as rand_float, randint
from constants.conferences import CONFERENCES
from constants.constants import MASSEY, HOME_FIELD_ADVANTAGE, CONFERENCES_WITHOUT_DIVISIONS
from constants.likelihoods import LIKELIHOODS
from constants.teams import TEAMS
from external_apis.cf_data import CFData
from ratings.inputs.data.massey_fcs import get_massey_rating_fcs_team
from ratings.inputs.data.team_ratings import TEAM_RATINGS


def trim_game(game: Dict) -> Dict:
    return {'home_team': game['home_team'], 'away_team': game['away_team'], 'neutral_site': game['neutral_site']}


def simulate_game(game):
    home_team, away_team = game['home_team'], game['away_team']
    winner, loser = (home_team, away_team) if game['home_team_win_pct'] > rand_float() else (away_team, home_team)
    are_both_teams_division_one = home_team in TEAMS and away_team in TEAMS
    is_conf_game = are_both_teams_division_one and TEAMS[home_team]['conference'] == TEAMS[away_team]['conference']
    return dict(winner=winner, loser=loser, is_conf_game=is_conf_game)


def add_ratings_to_game(game: Dict, team_ratings: Dict) -> Dict:
    adj_game = add_proj_margin_to_game(game, team_ratings)
    return adj_game


def get_net_power_rating(ratings: Dict) -> float:
    return mean([rating for rating in ratings.values()])


def determine_margin_for_game_vs_fcs_team(home_team, away_team):
    """Add a default margin if one of the teams is not rated by S&P+"""
    home_team_massey_rating = TEAM_RATINGS[home_team][MASSEY]
    away_team__massey_rating = get_massey_rating_fcs_team(away_team)
    return round(home_team_massey_rating + HOME_FIELD_ADVANTAGE - away_team__massey_rating, 1)


def add_proj_margin_to_game(game, team_ratings):
    home_team, away_team = game['home_team'], game['away_team']
    if home_team in team_ratings and away_team in team_ratings:
        home_team_ratings, away_team_ratings = team_ratings[home_team], team_ratings[away_team]
        game['away_team_rtgs'], game['home_team_rtgs'] = home_team_ratings, away_team_ratings
        # TODO: Running this every simulation --> could be cached
        ht_net_power, at_net_power = (get_net_power_rating(r) for r in (home_team_ratings, away_team_ratings))
        game['ht_net_power_rtg'], game['away_team_net_power_rtg'] = ht_net_power, at_net_power

        if not game['neutral_site']:
            game['home_team_projected_margin'] = round(ht_net_power + HOME_FIELD_ADVANTAGE - at_net_power, 1)
        else:
            game['home_team_projected_margin'] = round(ht_net_power - at_net_power, 1)

    else:
        game['home_team_projected_margin'] = determine_margin_for_game_vs_fcs_team(home_team, away_team)

    proj_margin = game['home_team_projected_margin']
    game['home_team_win_pct'] = LIKELIHOODS[proj_margin] if proj_margin > 0 else 1 - LIKELIHOODS[abs(proj_margin)]
    return game


def get_empty_wins_dict():
    return {x: 0 for x in range(14)}


def break_two_way_tie(team_one: str, team_two: str, simulated_season: List):
    teams = {team_one, team_two}
    game = [game for game in simulated_season if game['winner'] in teams and game['loser'] in teams]
    if game:
        return game[0]['winner']
    return team_one if rand_float() > 0.5 else team_two


def get_standings(conf_wins: Counter, teams: List):
    div_results_dict = defaultdict(list)
    div_win_totals = ((k, v) for k, v in conf_wins.items() if k in set(teams))
    for k, v in div_win_totals:
        div_results_dict[v].append(k)
    return div_results_dict


def get_top_two_teams(div_results_dict: DefaultDict, simulated_season: List):
    sorted_win_counts = sorted(div_results_dict.keys())
    max_wins = sorted_win_counts.pop()
    first_place_teams = div_results_dict[max_wins]
    first_place_teams_ct = len(first_place_teams)
    if first_place_teams_ct == 2:
        return first_place_teams
    if first_place_teams_ct == 1:
        second_most_wins = sorted_win_counts.pop()
        second_place_teams = div_results_dict[second_most_wins]
        second_place_teams_ct = len(second_place_teams)
        if second_place_teams_ct == 1:
            return first_place_teams + second_place_teams
        elif second_place_teams_ct == 2:
            second_place = break_two_way_tie(second_place_teams[0], second_place_teams[1], simulated_season)
            return first_place_teams + [second_place]
        else:
            rand_idx = randint(0, second_place_teams_ct - 1)
            second_place = second_place_teams[rand_idx]
            return first_place_teams + [second_place]

    # logic to handle 3+ way ties
    rand_idx = randint(0, first_place_teams_ct - 1)
    return [first_place_teams[rand_idx], first_place_teams[rand_idx - 1]]


def get_division_winners(divisions: Dict, conf_wins: Counter, simulated_season: List):
    # TODO: Refactor to only loop through conf_wins and simulated_season once
    res = []
    for div_name, division_teams in divisions.items():
        div_results_dict = get_standings(conf_wins, division_teams)

        max_wins = max(div_results_dict.keys())
        first_place_teams = div_results_dict[max_wins]
        first_place_teams_ct = len(first_place_teams)
        div_winner = None
        if first_place_teams_ct == 1:
            div_winner = first_place_teams.pop()
        elif first_place_teams_ct == 2:
            team_one, team_two = first_place_teams
            div_winner = break_two_way_tie(team_one, team_two, simulated_season)
        elif first_place_teams_ct >= 3:
            rand_idx = randint(0, first_place_teams_ct - 1)
            div_winner = first_place_teams[rand_idx]
        res.append(div_winner)
    return res


def get_title_game_participants(conf_wins: Counter, simulated_season: List, conf: str):
    conference_teams = CONFERENCES[conf]['teams']
    div_results_dict = get_standings(conf_wins, conference_teams)
    return get_top_two_teams(div_results_dict, simulated_season)


def get_average_opponent_rating_by_team(schedule):
    schedule_by_team = defaultdict(list)
    average_opponent_rating_by_team = dict()
    for game in schedule:
        ht, at = game['home_team'], game['away_team']
        if at in TEAM_RATINGS and at in TEAM_RATINGS:
            schedule_by_team[ht].append(at)
            schedule_by_team[at].append(ht)
    for team, schedule in schedule_by_team.items():
        opponent_ratings = [get_net_power_rating(TEAM_RATINGS[opponent]) for opponent in schedule]
        average_opponent_rating = sum(opponent_ratings) / len(opponent_ratings)
        average_opponent_rating_by_team[team] = round(average_opponent_rating, 2)
    return average_opponent_rating_by_team


class SimulateRegularSeason:
    def __init__(self, year: int, conference: Optional[str] = None):
        self.schedule = self.transform_schedule(year, conference)
        self.simulation_results = {
            team: {
                'conference_results': get_empty_wins_dict(),
                'non_conference_results': get_empty_wins_dict(),
                'total_wins': get_empty_wins_dict(),
                'division_title_count': 0,
                'conference_title_count': 0,
            }
            for team in TEAM_RATINGS.keys()
        }
        self.average_opponent_rating_by_team = get_average_opponent_rating_by_team(self.schedule)

    @staticmethod
    def transform_schedule(year: int, conference: Optional[str]):
        raw_schedule = CFData().get_schedule(year=year, conference=conference)
        trimmed_schedule = [trim_game(g) for g in raw_schedule]
        # TODO:
        # Consider passing a parameter here to add_ratings called `ratings_to_include`
        # and make it a set of the ratings that should be included in the simulation
        augmented_schedule = [add_ratings_to_game(game, TEAM_RATINGS) for game in trimmed_schedule]
        return augmented_schedule

    @staticmethod
    def get_division_winners_by_conf(conf_wins: Counter, simulated_season: List):
        division_winners_by_conf = {}
        for conf, conf_detail in CONFERENCES.items():
            if conf in CONFERENCES_WITHOUT_DIVISIONS:
                continue
            divisions = conf_detail.get('divisions')
            division_winners = get_division_winners(divisions, conf_wins, simulated_season)
            division_winners_by_conf[conf] = division_winners
        return division_winners_by_conf

    def increment_division_title_counts(self, division_winners: Dict):
        for winners in division_winners.values():
            for team in winners:
                self.simulation_results[team]['division_title_count'] += 1

    def increment_conference_title_coints(self, conference_winners: Set):
        for team in conference_winners:
            self.simulation_results[team]['conference_title_count'] += 1

    @staticmethod
    def simulate_conference_title_games(conf_wins: Counter, simulated_season: List, division_winners: Dict):
        conference_winners = set()
        for conf in CONFERENCES_WITHOUT_DIVISIONS - {'FBS Independents'}:
            title_game_participants = get_title_game_participants(conf_wins, simulated_season, conf)
            division_winners[conf] = title_game_participants
        for conf, title_game_participants in division_winners.items():
            team_one, team_two = title_game_participants
            conf_championship_game = dict(home_team=team_one, away_team=team_two, neutral_site=True)
            game_with_power_ratings = add_ratings_to_game(conf_championship_game, TEAM_RATINGS)
            res = simulate_game(game_with_power_ratings)
            conference_winners.add(res['winner'])
        return conference_winners

    def run(self, num_of_sims: int):
        for _ in range(num_of_sims):
            simulated_season = [simulate_game(game) for game in self.schedule]

            conf_games, nc_games, all_games = [], [], []
            for game in simulated_season:
                conf_games.append(game['winner']) if game['is_conf_game'] else nc_games.append(game['winner'])
                all_games.append(game['winner'])
            conf_wins, nc_wins, all_wins = Counter(conf_games), Counter(nc_games), Counter(all_games)
            total_wins = dict(conf_wins+nc_wins)

            for season_segment, results in (
                    ('conference_results', conf_wins), ('non_conference_results', nc_wins), ('total_wins', total_wins)):
                for k, v in results.items():
                    if self.simulation_results.get(k):
                        self.simulation_results[k][season_segment][v] += 1

            # TODO: Consider transforming simulated_season to key by team
            division_winners = self.get_division_winners_by_conf(conf_wins, simulated_season)
            self.increment_division_title_counts(division_winners)

            conference_winners = self.simulate_conference_title_games(conf_wins, simulated_season, division_winners)
            self.increment_conference_title_coints(conference_winners)


# # TODO: Simulation results appear to be underestimating good teams --> see Ohio State and Michigan, are they working?
# s = SimulateRegularSeason(year=2019)
# s.run(1)
# print(s.simulation_results)
