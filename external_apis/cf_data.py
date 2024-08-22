import requests
import cfbd

BASE_CFD_API = "https://api.collegefootballdata.com"

class CFData:
    def __init__(self):
        configuration = cfbd.Configuration()
        configuration.api_key['Authorization'] = 'v5TLyLl9pmeFDqKog4FsFwj2gv8x5Pwat4G6fqJf4SCBEsrbL93Xgcgz2gLXVC0f'
        configuration.api_key_prefix['Authorization'] = 'Bearer'

        self.base_path = BASE_CFD_API
        self.api_instance = cfbd.GamesApi(cfbd.ApiClient(configuration))
        self.teams_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))

    def get_schedule(self, year: int, conference: str):
        if conference:
            return self.api_instance.get_games(year=year, conference=conference).json()
        return self.api_instance.get_games(year=year) # .json()

    def get_teams(self):
        return self.teams_instance.get_teams()
