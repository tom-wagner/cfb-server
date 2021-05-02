from typing import Dict, List, Optional, DefaultDict, Set
from statistics import mean
from collections import Counter, defaultdict
from random import random as rand_float, randint
from constants.conferences import CONFERENCES
from constants.constants import MASSEY, HOME_FIELD_ADVANTAGE, CONFERENCES_WITHOUT_DIVISIONS, RANKING_SYSTEMS
from constants.likelihoods import LIKELIHOODS
from constants.teams import TEAMS
from external_apis.cf_data import CFData
# from ratings.inputs.data.massey_fcs import get_massey_rating_fcs_team
from ratings.inputs.data.team_ratings.this_year.preseason import TEAM_RATINGS as TR_PRESEASON


def trim_game(game: Dict) -> Dict:
    return {'home_team': game['home_team'], 'away_team': game['away_team'], 'neutral_site': game['neutral_site'],
            'start_date': game['start_date'], 'home_points': game['home_points'], 'away_points': game['away_points']}


def simulate_game(game):
    home_team, away_team = game['home_team'], game['away_team']
    if game.get('home_points') is not None:
        winner, loser = (home_team, away_team) if game['home_points'] > game['away_points'] else (away_team, home_team)
    else:
        winner, loser = (home_team, away_team) if game['home_team_win_pct'] > rand_float() else (away_team, home_team)
    are_both_teams_division_one = home_team in TEAMS and away_team in TEAMS
    is_conf_game = are_both_teams_division_one and TEAMS[home_team]['conference'] == TEAMS[away_team]['conference']
    return dict(winner=winner, loser=loser, is_conf_game=is_conf_game)


def add_ratings_to_game(game: Dict, team_ratings: Dict) -> Dict:
    adj_game = add_proj_margin_to_game(game, team_ratings)
    return adj_game


# TODO: Adding logic to filter out ratings systems wouldn't be that hard
def get_net_power_rating(ratings: Dict) -> float:
    return round(mean([rating for rating in ratings.values()]), 2)


def determine_margin_for_game_vs_fcs_team(home_team, away_team, team_ratings):
    """Add a default margin if one of the teams is not rated by S&P+"""
    # home_team_massey_rating = team_ratings[home_team][MASSEY]
    # away_team__massey_rating = get_massey_rating_fcs_team(away_team)
    # return round(home_team_massey_rating + HOME_FIELD_ADVANTAGE - away_team__massey_rating, 1)

    # Don't have Massey yet, setting arbitrarily high
    return 35



def add_proj_margin_to_game(game, team_ratings):
    home_team, away_team = game['home_team'], game['away_team']

    # handle already played games
    if game.get('home_points') is not None:
        game['home_team_win_pct'] = 1 if game['home_points'] > game['away_points'] else 0
        return game

    if home_team in team_ratings and away_team in team_ratings:
        home_team_ratings, away_team_ratings = team_ratings[home_team], team_ratings[away_team]
        game['away_team_rtgs'], game['home_team_rtgs'] = home_team_ratings, away_team_ratings
        ht_net_power, at_net_power = (r['avg_power_rtg'] for r in (home_team_ratings, away_team_ratings))
        game['ht_net_power_rtg'], game['away_team_net_power_rtg'] = ht_net_power, at_net_power

        if not game['neutral_site']:
            game['home_team_projected_margin'] = round(ht_net_power + HOME_FIELD_ADVANTAGE - at_net_power, 1)
        else:
            game['home_team_projected_margin'] = round(ht_net_power - at_net_power, 1)

    else:
        game['home_team_projected_margin'] = determine_margin_for_game_vs_fcs_team(home_team, away_team, team_ratings)

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


def get_average_opponent_rating_by_team(schedule: List, team_ratings: Dict):
    schedule_by_team = defaultdict(list)
    average_opponent_rating_by_team = dict()
    for game in schedule:
        ht, at = game['home_team'], game['away_team']
        if at in team_ratings and at in team_ratings:
            schedule_by_team[ht].append(at)
            schedule_by_team[at].append(ht)

    for team, schedule in schedule_by_team.items():
        # adding -35 for FCS teams
        opponent_ratings = [
            team_ratings[opponent]['avg_power_rtg'] if team_ratings.get(opponent) != None else -35
            for opponent in schedule]
        average_opponent_rating = sum(opponent_ratings) / len(opponent_ratings)
        average_opponent_rating_by_team[team] = round(average_opponent_rating, 2)

    return average_opponent_rating_by_team


def add_average_rating(team_ratings: Dict) -> Dict:
    return {team: {'avg_power_rtg': get_net_power_rating(ratings), **ratings} for team, ratings in team_ratings.items()}


def f(team_ratings: Dict, rating_system: str) -> Dict:
    sorted_tuples = sorted([(team, power_ratings[rating_system]) for team, power_ratings in team_ratings.items()],
                           key=lambda tup: tup[1], reverse=True)
    return {team: idx + 1 for idx, (team, _) in enumerate(sorted_tuples)}


def get_rankings_by_rating_system(team_ratings: Dict) -> Dict:
    systems_to_rank_by = RANKING_SYSTEMS | {'avg_power_rtg'}
    return {rating_system: f(team_ratings, rating_system) for rating_system in systems_to_rank_by}


def get_rankings_for_team(team: str, rankings: Dict) -> Dict:
    return {rating_system_name: rating_system_rankings[team] for rating_system_name, rating_system_rankings in
            rankings.items()}


class SimulateRegularSeason:
    def __init__(self, year: Optional[int] = 2021, num_of_sims: int = 1000, conference: Optional[str] = None):
        self.ratings = add_average_rating(TR_PRESEASON)
        self.rankings = get_rankings_by_rating_system(self.ratings)
        self.schedule = self.transform_schedule(year, conference)
        self.num_of_sims = num_of_sims
        self.simulation_results = {
            team: {
                'schedule': [game for game in self.schedule if team == game['away_team'] or team == game['home_team']],
                'rankings': get_rankings_for_team(team, self.rankings),
                'conference_results': get_empty_wins_dict(),
                'non_conference_results': get_empty_wins_dict(),
                'total_wins': get_empty_wins_dict(),
                'division_title_count': 0,
                'conference_title_count': 0,
                'conference_title_win_pct': None,
                'division_title_win_pct': None,
            }
            for team in self.ratings.keys()
        }
        self.average_opponent_rating_by_team = get_average_opponent_rating_by_team(self.schedule, self.ratings)

    def calculate_percentages(self):
        conferences_without_divisions = {'FBS Independents', 'Sun Belt', 'Big 12'}
        for team in TEAMS:
            conference = TEAMS[team]['conference']
            if conference not in conferences_without_divisions:
                division_title_ct = self.simulation_results[team]['division_title_count']
                self.simulation_results[team]['division_title_win_pct'] = round(division_title_ct / self.num_of_sims, 4)
            else:
                self.simulation_results[team]['division_title_win_pct'] = -1

            if conference != 'FBS Independents':
                conf_title_ct = self.simulation_results[team]['conference_title_count']
                self.simulation_results[team]['conference_title_win_pct'] = round(conf_title_ct / self.num_of_sims, 4)
            else:
                self.simulation_results[team]['conference_title_win_pct'] = -1

    # TODO for v1 --> don't make this API call and instead have a constant
    def transform_schedule(self, year: int, conference: Optional[str]):
        raw_schedule = CFData().get_schedule(year=year, conference=conference)

        # TODO: remove this hack --> https://twitter.com/messages/84006766-1158580518134456321
        # NOTE: still 2x New Mexico game as of 12/6
        raw_schedule_filtered_for_af_reschedule = [g for g in raw_schedule if g['id'] != 401117539]

        # TODO: Evaluate whether this needs to be here for next year
        # TODO: Get rid of this hack too --> add logic for differentiating reg season and conf championships next year
        # g['id'] hack is for army/navy (which is in week 15)
        reg_season = [g for g in raw_schedule_filtered_for_af_reschedule if g['week'] != 15 or g['id'] == 401114335]

        trimmed_schedule = [trim_game(g) for g in reg_season]

        # TODO:
        # Consider passing a parameter here to add_ratings called `ratings_to_include`
        # and make it a set of the ratings that should be included in the simulation
        augmented_schedule = [add_ratings_to_game(game, self.ratings) for game in trimmed_schedule]
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

    def simulate_conference_title_games(self, conf_wins: Counter, simulated_season: List, division_winners: Dict):
        conference_winners = set()
        for conf in CONFERENCES_WITHOUT_DIVISIONS - {'FBS Independents'}:
            title_game_participants = get_title_game_participants(conf_wins, simulated_season, conf)
            division_winners[conf] = title_game_participants
        for conf, title_game_participants in division_winners.items():
            team_one, team_two = title_game_participants
            conf_championship_game = dict(home_team=team_one, away_team=team_two, neutral_site=True)
            game_with_power_ratings = add_ratings_to_game(conf_championship_game, self.ratings)
            res = simulate_game(game_with_power_ratings)
            conference_winners.add(res['winner'])
        return conference_winners

    def run(self):
        for _ in range(self.num_of_sims):
            simulated_season = [simulate_game(game) for game in self.schedule]

            conf_games, nc_games, all_games = [], [], []
            for game in simulated_season:
                conf_games.append(game['winner']) if game['is_conf_game'] else nc_games.append(game['winner'])
                all_games.append(game['winner'])
            conf_wins, nc_wins, all_wins = Counter(conf_games), Counter(nc_games), Counter(all_games)
            total_wins = dict(conf_wins + nc_wins)

            # add winless teams:
            for team in self.ratings.keys():
                if team not in total_wins:
                    nc_wins[team], conf_wins[team], total_wins[team] = 0, 0, 0

            for season_segment, results in (
                    ('conference_results', conf_wins), ('non_conference_results', nc_wins), ('total_wins', total_wins)):
                for k, v in results.items():
                    if k in self.simulation_results:
                        self.simulation_results[k][season_segment][v] += 1

            # TODO: Consider transforming simulated_season to key by team
            division_winners = self.get_division_winners_by_conf(conf_wins, simulated_season)
            self.increment_division_title_counts(division_winners)

            conference_winners = self.simulate_conference_title_games(conf_wins, simulated_season, division_winners)
            self.increment_conference_title_coints(conference_winners)

        self.calculate_percentages()


s = SimulateRegularSeason(num_of_sims=10000)
s.run()

print(s.simulation_results)
