# NOTE --> AVERAGING TOGETHER IS SAME AS CALCULATING ONE BY ONE --> SEE LOGIC AT END OF FILE

# NOTE --> KNOWN BUG WITH MIAMI (OH) vs Miami FPI ratings

# James Madison is a manual hack as of now
# 2022
# TEAM_RATINGS = {'Air Force': {'SP_PLUS': 4.9}, 'Akron': {'SP_PLUS': -22.0}, 'Alabama': {'SP_PLUS': 32.2}, 'Appalachian State': {'SP_PLUS': 4.1}, 'Arizona': {'SP_PLUS': -10.5}, 'Arizona State': {'SP_PLUS': 5.8}, 'Arkansas': {'SP_PLUS': 16.3}, 'Arkansas State': {'SP_PLUS': -17.0}, 'Army': {'SP_PLUS': -0.6}, 'Auburn': {'SP_PLUS': 14.4}, 'Ball State': {'SP_PLUS': -11.4}, 'Baylor': {'SP_PLUS': 12.9}, 'Boise State': {'SP_PLUS': 9.9}, 'Boston College': {'SP_PLUS': 0.3}, 'Bowling Green': {'SP_PLUS': -12.7}, 'Buffalo': {'SP_PLUS': -11.1}, 'BYU': {'SP_PLUS': 13.9}, 'California': {'SP_PLUS': -2.0}, 'Central Michigan': {'SP_PLUS': -4.0}, 'Charlotte': {'SP_PLUS': -12.6}, 'Cincinnati': {'SP_PLUS': 16.1}, 'Clemson': {'SP_PLUS': 21.4}, 'Coastal Carolina': {'SP_PLUS': -0.3}, 'Colorado': {'SP_PLUS': -7.1}, 'Colorado State': {'SP_PLUS': -7.6}, 'Connecticut': {'SP_PLUS': -24.9}, 'Duke': {'SP_PLUS': -16.0}, 'East Carolina': {'SP_PLUS': -0.7}, 'Eastern Michigan': {'SP_PLUS': -8.4}, 'Florida': {'SP_PLUS': 13.8}, 'Florida Atlantic': {'SP_PLUS': -8.5}, 'Florida International': {'SP_PLUS': -26.2}, 'Florida State': {'SP_PLUS': 8.4}, 'Fresno State': {'SP_PLUS': 7.9}, 'Georgia': {'SP_PLUS': 30.5}, 'Georgia Southern': {'SP_PLUS': -14.0}, 'Georgia State': {'SP_PLUS': -1.5}, 'Georgia Tech': {'SP_PLUS': -5.5}, "Hawai'i": {'SP_PLUS': -19.2}, 'Houston': {'SP_PLUS': 10.3}, 'Illinois': {'SP_PLUS': -2.4}, 'Indiana': {'SP_PLUS': -5.0}, 'Iowa': {'SP_PLUS': 13.3}, 'Iowa State': {'SP_PLUS': 6.9}, 'James Madison': {'SP_PLUS': -7.5}, 'Kansas': {'SP_PLUS': -10.4}, 'Kansas State': {'SP_PLUS': 10.0}, 'Kent State': {'SP_PLUS': -11.1}, 'Kentucky': {'SP_PLUS': 16.8}, 'Louisiana': {'SP_PLUS': 0.7}, 'Louisiana Monroe': {'SP_PLUS': -21.3}, 'Louisiana Tech': {'SP_PLUS': -12.9}, 'Louisville': {'SP_PLUS': 9.3}, 'LSU': {'SP_PLUS': 13.2}, 'Marshall': {'SP_PLUS': 1.0}, 'Maryland': {'SP_PLUS': 4.1}, 'Memphis': {'SP_PLUS': 1.8}, 'Miami': {'SP_PLUS': 13.2}, 'Miami (OH)': {'SP_PLUS': -4.4}, 'Michigan': {'SP_PLUS': 21.4}, 'Michigan State': {'SP_PLUS': 16.1}, 'Middle Tennessee': {'SP_PLUS': -8.6}, 'Minnesota': {'SP_PLUS': 12.4}, 'Mississippi State': {'SP_PLUS': 14.7}, 'Missouri': {'SP_PLUS': 5.9}, 'Navy': {'SP_PLUS': -10.8}, 'NC State': {'SP_PLUS': 15.4}, 'Nebraska': {'SP_PLUS': 8.3}, 'Nevada': {'SP_PLUS': -13.4}, 'New Mexico': {'SP_PLUS': -20.8}, 'North Carolina': {'SP_PLUS': 9.4}, 'Northern Illinois': {'SP_PLUS': -4.3}, 'North Texas': {'SP_PLUS': -5.6}, 'Northwestern': {'SP_PLUS': -5.6}, 'Notre Dame': {'SP_PLUS': 21.0}, 'Ohio': {'SP_PLUS': -12.4}, 'Ohio State': {'SP_PLUS': 29.7}, 'Oklahoma': {'SP_PLUS': 22.5}, 'Oklahoma State': {'SP_PLUS': 14.9}, 'Old Dominion': {'SP_PLUS': -7.5}, 'Ole Miss': {'SP_PLUS': 17.9}, 'Oregon': {'SP_PLUS': 14.3}, 'Oregon State': {'SP_PLUS': 3.8}, 'Penn State': {'SP_PLUS': 16.5}, 'Pittsburgh': {'SP_PLUS': 14.4}, 'Purdue': {'SP_PLUS': 9.9}, 'Rice': {'SP_PLUS': -16.7}, 'Rutgers': {'SP_PLUS': -2.7}, 'San Diego State': {'SP_PLUS': 3.3}, 'San José State': {'SP_PLUS': -7.6}, 'SMU': {'SP_PLUS': 8.4}, 'South Alabama': {'SP_PLUS': -11.3}, 'South Carolina': {'SP_PLUS': 9.4}, 'Southern Mississippi': {'SP_PLUS': -9.1}, 'South Florida': {'SP_PLUS': -5.7}, 'Stanford': {'SP_PLUS': -1.0}, 'Syracuse': {'SP_PLUS': 1.8}, 'TCU': {'SP_PLUS': 8.4}, 'Temple': {'SP_PLUS': -19.4}, 'Tennessee': {'SP_PLUS': 17.3}, 'Texas': {'SP_PLUS': 14.4}, 'Texas A&M': {'SP_PLUS': 19.5}, 'Texas State': {'SP_PLUS': -18.8}, 'Texas Tech': {'SP_PLUS': 6.3}, 'Toledo': {'SP_PLUS': 2.5}, 'Troy': {'SP_PLUS': -7.0}, 'Tulane': {'SP_PLUS': -4.0}, 'Tulsa': {'SP_PLUS': -4.3}, 'UAB': {'SP_PLUS': 3.1}, 'UCF': {'SP_PLUS': 8.5}, 'UCLA': {'SP_PLUS': 9.8}, 'UMass': {'SP_PLUS': -26.5}, 'UNLV': {'SP_PLUS': -13.9}, 'USC': {'SP_PLUS': 7.2}, 'Utah': {'SP_PLUS': 16.5}, 'Utah State': {'SP_PLUS': -1.8}, 'UTEP': {'SP_PLUS': -9.5}, 'UT San Antonio': {'SP_PLUS': 5.8}, 'Vanderbilt': {'SP_PLUS': -11.3}, 'Virginia': {'SP_PLUS': 1.7}, 'Virginia Tech': {'SP_PLUS': 2.6}, 'Wake Forest': {'SP_PLUS': 7.0}, 'Washington': {'SP_PLUS': 3.6}, 'Washington State': {'SP_PLUS': 0.4}, 'Western Kentucky': {'SP_PLUS': 1.3}, 'Western Michigan': {'SP_PLUS': -7.7}, 'West Virginia': {'SP_PLUS': 3.3}, 'Wisconsin': {'SP_PLUS': 15.6}, 'Wyoming': {'SP_PLUS': -11.7}, 'New Mexico State': {'SP_PLUS': -27.4}, 'Liberty': {'SP_PLUS': -1.1}}

# KNOWN TEAM ISSUES
# All "State"

TEAM_RATINGS = {
    "Georgia": {
        "SP_PLUS": 34.2
    },
    "Ohio State": {
        "SP_PLUS": 30.8
    },
    "Oregon": {
        "SP_PLUS": 29
    },
    "Alabama": {
        "SP_PLUS": 27.8
    },
    "Texas": {
        "SP_PLUS": 27.7
    },
    "Penn State": {
        "SP_PLUS": 26.1
    },
    "Michigan": {
        "SP_PLUS": 25
    },
    "Ole Miss": {
        "SP_PLUS": 24.7
    },
    "Notre Dame": {
        "SP_PLUS": 23.4
    },
    "LSU": {
        "SP_PLUS": 23.1
    },
    "Missouri": {
        "SP_PLUS": 22.2
    },
    "Florida State": {
        "SP_PLUS": 19.9
    },
    "Oklahoma": {
        "SP_PLUS": 19.8
    },
    "Texas A&M": {
        "SP_PLUS": 19.2
    },
    "Tennessee": {
        "SP_PLUS": 19.2
    },
    "Clemson": {
        "SP_PLUS": 18.8
    },
    "Kansas State": {
        "SP_PLUS": 16.4
    },
    "Utah": {
        "SP_PLUS": 15.8
    },
    "Miami": {
        "SP_PLUS": 15.5
    },
    "Oklahoma State": {
        "SP_PLUS": 14
    },
    "USC": {
        "SP_PLUS": 13.9
    },
    "Kentucky": {
        "SP_PLUS": 13.8
    },
    "Florida": {
        "SP_PLUS": 13.2
    },
    "Iowa": {
        "SP_PLUS": 13.2
    },
    "Auburn": {
        "SP_PLUS": 13.1
    },
    "Wisconsin": {
        "SP_PLUS": 12.9
    },
    "SMU": {
        "SP_PLUS": 12.7
    },
    "Arizona": {
        "SP_PLUS": 12.4
    },
    "NC State": {
        "SP_PLUS": 12.1
    },
    "Iowa State": {
        "SP_PLUS": 11.5
    },
    "Louisville": {
        "SP_PLUS": 11.3
    },
    "Washington": {
        "SP_PLUS": 10.3
    },
    "Kansas": {
        "SP_PLUS": 9.7
    },
    "West Virginia": {
        "SP_PLUS": 9.7
    },
    "South Carolina": {
        "SP_PLUS": 9.5
    },
    "Virginia Tech": {
        "SP_PLUS": 9.4
    },
    "UCLA": {
        "SP_PLUS": 8.8
    },
    "TCU": {
        "SP_PLUS": 8.7
    },
    "Boise State": {
        "SP_PLUS": 7.9
    },
    "North Carolina": {
        "SP_PLUS": 7.9
    },
    "Texas Tech": {
        "SP_PLUS": 7.4
    },
    "Nebraska": {
        "SP_PLUS": 7.4
    },
    "Memphis": {
        "SP_PLUS": 6.1
    },
    "Arkansas": {
        "SP_PLUS": 6.1
    },
    "UCF": {
        "SP_PLUS": 5.9
    },
    "Maryland": {
        "SP_PLUS": 5.2
    },
    "Minnesota": {
        "SP_PLUS": 4.2
    },
    "Liberty": {
        "SP_PLUS": 3.9
    },
    "Rutgers": {
        "SP_PLUS": 3.5
    },
    "Oregon State": {
        "SP_PLUS": 3.2
    },
    "Duke": {
        "SP_PLUS": 3.1
    },
    "California": {
        "SP_PLUS": 2.8
    },
    "Baylor": {
        "SP_PLUS": 2.2
    },
    "UT San Antonio": {
        "SP_PLUS": 1.2
    },
    "Mississippi State": {
        "SP_PLUS": 1.1
    },
    "JMU": {
        "SP_PLUS": 0.7
    },
    "Washington State": {
        "SP_PLUS": 0.6
    },
    "Georgia Tech": {
        "SP_PLUS": 0.6
    },
    "Appalachian State": {
        "SP_PLUS": 0.5
    },
    "Colorado": {
        "SP_PLUS": 0.3
    },
    "Illinois": {
        "SP_PLUS": 0.1
    },
    "Cincinnati": {
        "SP_PLUS": -0.1
    },
    "Fresno State": {
        "SP_PLUS": -0.1
    },
    "Troy": {
        "SP_PLUS": -0.7
    },
    "Tulane": {
        "SP_PLUS": -0.8
    },
    "Pittsburgh": {
        "SP_PLUS": -0.8
    },
    "Syracuse": {
        "SP_PLUS": -1
    },
    "Purdue": {
        "SP_PLUS": -1.4
    },
    "BYU": {
        "SP_PLUS": -1.5
    },
    "Western Kentucky": {
        "SP_PLUS": -1.6
    },
    "Michigan State": {
        "SP_PLUS": -2.4
    },
    "Louisiana": {
        "SP_PLUS": -2.4
    },
    "Boston College": {
        "SP_PLUS": -2.4
    },
    "Wake Forest": {
        "SP_PLUS": -2.6
    },
    "Northwestern": {
        "SP_PLUS": -2.8
    },
    "Houston": {
        "SP_PLUS": -3.3
    },
    "Stanford": {
        "SP_PLUS": -3.5
    },
    "Virginia": {
        "SP_PLUS": -3.5
    },
    "Arizona State": {
        "SP_PLUS": -4
    },
    "Miami (OH)": {
        "SP_PLUS": -4
    },
    "Indiana": {
        "SP_PLUS": -4.5
    },
    "UNLV": {
        "SP_PLUS": -5.2
    },
    "South Florida": {
        "SP_PLUS": -5.6
    },
    "South Alabama": {
        "SP_PLUS": -6.4
    },
    "Coastal Carolina": {
        "SP_PLUS": -6.5
    },
    "Texas State": {
        "SP_PLUS": -6.5
    },
    "Toledo": {
        "SP_PLUS": -7
    },
    "Air Force": {
        "SP_PLUS": -7.1
    },
    "Vanderbilt": {
        "SP_PLUS": -7.3
    },
    "Wyoming": {
        "SP_PLUS": -8
    },
    "San Diego State": {
        "SP_PLUS": -8.9
    },
    "Rice": {
        "SP_PLUS": -9
    },
    "Arkansas State": {
        "SP_PLUS": -9.1
    },
    "East Carolina": {
        "SP_PLUS": -9.5
    },
    "Marshall": {
        "SP_PLUS": -9.9
    },
    "Jacksonville State": {
        "SP_PLUS": -9.9
    },
    "Georgia Southern": {
        "SP_PLUS": -10.3
    },
    "Northern Illinois": {
        "SP_PLUS": -10.6
    },
    "UAB": {
        "SP_PLUS": -10.6
    },
    "Colorado State": {
        "SP_PLUS": -10.6
    },
    "San José State": {
        "SP_PLUS": -11
    },
    "Utah State": {
        "SP_PLUS": -11.1
    },
    "Army": {
        "SP_PLUS": -11.1
    },
    "Bowling Green": {
        "SP_PLUS": -11.2
    },
    "North Texas": {
        "SP_PLUS": -11.3
    },
    "Georgia State": {
        "SP_PLUS": -11.3
    },
    "Ohio": {
        "SP_PLUS": -12
    },
    "Florida Atlantic": {
        "SP_PLUS": -12.2
    },
    "Hawai'i": {
        "SP_PLUS": -12.6
    },
    "Western Michigan": {
        "SP_PLUS": -12.9
    },
    "Old Dominion": {
        "SP_PLUS": -13.1
    },
    "Tulsa": {
        "SP_PLUS": -13.2
    },
    "Navy": {
        "SP_PLUS": -13.3
    },
    "Middle Tennessee": {
        "SP_PLUS": -13.4
    },
    "Sam Houston": {
        "SP_PLUS": -14.2
    },
    "New Mexico State": {
        "SP_PLUS": -15.5
    },
    "Central Michigan": {
        "SP_PLUS": -15.9
    },
    "Eastern Michigan": {
        "SP_PLUS": -15.9
    },
    "Southern Mississippi": {
        "SP_PLUS": -16.1
    },
    "Louisiana Tech": {
        "SP_PLUS": -16.7
    },
    "Nevada": {
        "SP_PLUS": -16.7
    },
    "Ball State": {
        "SP_PLUS": -16.9
    },
    "Buffalo": {
        "SP_PLUS": -17
    },
    "UTEP": {
        "SP_PLUS": -17.8
    },
    "Connecticut": {
        "SP_PLUS": -17.9
    },
    "Charlotte": {
        "SP_PLUS": -18.1
    },
    "Florida International": {
        "SP_PLUS": -19
    },
    "UMass": {
        "SP_PLUS": -20.1
    },
    "New Mexico": {
        "SP_PLUS": -20.6
    },
    "Kent State": {
        "SP_PLUS": -20.9
    },
    "Kennesaw State": {
        "SP_PLUS": -20.9
    },
    "Temple": {
        "SP_PLUS": -21.9
    },
    "Akron": {
        "SP_PLUS": -22.2
    },
    "Louisiana Monroe": {
        "SP_PLUS": -23.4
    },
    # NEW TEAMS HERE
    "Samford": {
        "SP_PLUS": -17
    }
};

# 2024 NOTES --> Two Column team name, rating as CSV starting point (use mid function in Excel); then use CSV JSON --> then use code snippet in google chrome

# teams.reduce((acc, cv) => {
#     return { ...acc, [cv.Team]: { 'SP_PLUS': cv.SP_PLUS } };
# }, {})




# LOGIC FOR AVERAGING VS CALCULATING ONE BY ONE
# mn = TEAM_RATINGS['Minnesota']
# wi = TEAM_RATINGS['Wisconsin']
#
# mn_average, wi_average = (sum(d.values()) / len(d.values()) for d in (mn, wi))
#
# print(mn_average, wi_average)
#
# print(mn, wi)
# mn_diff = [x - y for x, y in list(zip(mn.values(), wi.values()))]
#
# print(sum(mn_diff) / 4)
# print(mn_average - wi_average)
