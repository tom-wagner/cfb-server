from flask import Flask, json, request
from flask_cors import CORS

from constants.conferences import CONFERENCES
from constants.teams import TEAMS
from external_apis.cf_data import CFData
from ratings.inputs.data.team_ratings import TEAM_RATINGS
from simulate.simulate_regular_season import SimulateRegularSeason

app = Flask(__name__)
CORS(app)


# TODO: Improve error handling and consider moving to CFData file or base_api.py file
# https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module

# TODO: Clean up repeated logic


@app.route("/team_ratings", methods=['GET'])
def team_ratings():
    return json.jsonify(TEAM_RATINGS)


@app.route("/teams", methods=['GET'])
def teams():
    try:
        adj_teams_object = {
            team: dict(
                power_rtgs=TEAM_RATINGS[team],
                avg_power_rtg=round(sum([rtg for rtg in TEAM_RATINGS[team].values()]) / len(TEAM_RATINGS[team]), 1),
                **team_obj,
            )
            for team, team_obj in TEAMS.items()
        }
        return json.jsonify(adj_teams_object)
    except Exception as e:
        return dict(error="Error fetching teams", detail=e)


@app.route("/schedule", methods=['GET'])
def schedule():
    try:
        res = CFData().get_schedule(year=request.args.get('year'))
        return json.jsonify(res)
    except Exception as e:
        return dict(error="Error fetching schedule", detail=e)


@app.route("/conferences", methods=['GET'])
def conferences():
    return json.jsonify(CONFERENCES)


@app.route("/simulate", methods=["GET"])
def simulate():
    # year, conference = (request.args.get(arg) for arg in ('year', 'conference'))
    s = SimulateRegularSeason()
    s.run()
    return json.jsonify(dict(simulation_results=s.simulation_results, num_of_sims=s.num_of_sims))


app.run(debug=True)
