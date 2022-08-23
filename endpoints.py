from flask import Flask, json, request
from flask_cors import CORS

from constants.conferences import CONFERENCES
from constants.simulation_results.twenty_twenty_two.aug_seventeenth import aug_seventeenth
from constants.teams import TEAMS
from external_apis.cf_data import CFData
from ratings.inputs.data.team_ratings.twenty_twenty_two.preseason import TEAM_RATINGS as TR_PRESEASON

# FOR RUNNING REAL-TIME
# from simulate.simulate_regular_season import SimulateRegularSeason

app = Flask(__name__)
CORS(app)


# TODO: Improve error handling and consider moving to CFData file or base_api.py file
# https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module

# TODO: Clean up repeated logic

@app.route("/", methods=["GET"])
def get_slash():
    return dict(running=True)


@app.route("/team_ratings", methods=['GET'])
def team_ratings():
    return json.jsonify(TR_PRESEASON)


@app.route("/teams", methods=['GET'])
def teams():
    try:
        adj_teams_object = {
            team: dict(
                power_rtgs=TR_PRESEASON[team],
                avg_power_rtg=round(sum([rtg for rtg in TR_PRESEASON[team].values()]) / len(TR_PRESEASON[team]), 1),
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
    return json.jsonify(aug_seventeenth)


# TO ACTUALLY RUN ON POST
# @app.route("/simulate", methods=["GET"])
# def simulate():
#     # year, conference = (request.args.get(arg) for arg in ('year', 'conference'))
#     s = SimulateRegularSeason()
#     print(s)
#     s.run()
#     return json.jsonify(
#         dict(simulation_results=s.simulation_results, num_of_sims=s.num_of_sims, simulation_expiration='',
#              warning_message=''))


if __name__ == '__main__':
    app.run()

# app.run(debug=True)
