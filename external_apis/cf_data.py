import requests

BASE_CFD_API = "https://api.collegefootballdata.com"


class CFData:
    def __init__(self):
        self.base_path = BASE_CFD_API

    def get(self, route: str, **params):
        return requests.get(
            f'{self.base_path}/{route}',
            params=params,
            headers={'Authorization': 'Bearer v5TLyLl9pmeFDqKog4FsFwj2gv8x5Pwat4G6fqJf4SCBEsrbL93Xgcgz2gLXVC0f'})

    def get_schedule(self, year: int, conference: str):
        if conference:
            return self.get("games", year=year, conference=conference).json()
        return self.get("games", year=year).json()

    def get_teams(self):
        return self.get("teams").json()
