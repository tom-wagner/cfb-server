# NOTE --> AVERAGING TOGETHER IS SAME AS CALCULATING ONE BY ONE --> SEE LOGIC AT END OF FILE

# NOTE --> KNOWN BUG WITH MIAMI (OH) vs Miami FPI ratings

TEAM_RATINGS = {'Air Force': {'SP_PLUS': -3.5, 'FPI': -1.5, 'ENTROPY': 46.77, 'MASSEY': 53.76},
                'Akron': {'SP_PLUS': -19.9, 'FPI': -16.5, 'ENTROPY': 26.72, 'MASSEY': 41.29},
                'Alabama': {'SP_PLUS': 35.4, 'FPI': 27.9, 'ENTROPY': 81.27, 'MASSEY': 87.66},
                'Appalachian State': {'SP_PLUS': 10.4, 'FPI': -0.2, 'ENTROPY': 52.46, 'MASSEY': 62.49},
                'Arizona': {'SP_PLUS': 5.4, 'FPI': 3.7, 'ENTROPY': 49.76, 'MASSEY': 56.66},
                'Arizona State': {'SP_PLUS': 5.9, 'FPI': 7.4, 'ENTROPY': 52.96, 'MASSEY': 60.43},
                'Arkansas': {'SP_PLUS': 6.1, 'FPI': 0.5, 'ENTROPY': 44.75, 'MASSEY': 52.35},
                'Arkansas State': {'SP_PLUS': 1.0, 'FPI': -5.8, 'ENTROPY': 43.32, 'MASSEY': 52.1},
                'Army': {'SP_PLUS': -1.4, 'FPI': -1.2, 'ENTROPY': 45.6, 'MASSEY': 62.05},
                'Auburn': {'SP_PLUS': 22.6, 'FPI': 16.8, 'ENTROPY': 65.3, 'MASSEY': 73.78},
                'Ball State': {'SP_PLUS': -12.9, 'FPI': -10.7, 'ENTROPY': 35.67, 'MASSEY': 39.83},
                'Baylor': {'SP_PLUS': 8.1, 'FPI': 8.5, 'ENTROPY': 52.13, 'MASSEY': 61.16},
                'Boise State': {'SP_PLUS': 12.6, 'FPI': 5.9, 'ENTROPY': 60.25, 'MASSEY': 65.88},
                'Boston College': {'SP_PLUS': 0.7, 'FPI': -0.3, 'ENTROPY': 50.0, 'MASSEY': 64.51},
                'Bowling Green': {'SP_PLUS': -19.4, 'FPI': -15.2, 'ENTROPY': 26.58, 'MASSEY': 39.97},
                'Buffalo': {'SP_PLUS': -7.0, 'FPI': -11.9, 'ENTROPY': 37.95, 'MASSEY': 54.25},
                'BYU': {'SP_PLUS': 5.7, 'FPI': 5.5, 'ENTROPY': 52.12, 'MASSEY': 59.74},
                'California': {'SP_PLUS': 3.4, 'FPI': 2.2, 'ENTROPY': 48.82, 'MASSEY': 58.52},
                'Central Michigan': {'SP_PLUS': -18.5, 'FPI': -14.5, 'ENTROPY': 28.31, 'MASSEY': 39.21},
                'Charlotte': {'SP_PLUS': -17.8, 'FPI': -15.0, 'ENTROPY': 26.84, 'MASSEY': 43.97},
                'Cincinnati': {'SP_PLUS': 7.1, 'FPI': 6.4, 'ENTROPY': 52.55, 'MASSEY': 59.44},
                'Clemson': {'SP_PLUS': 29.9, 'FPI': 29.2, 'ENTROPY': 80.05, 'MASSEY': 95.38},
                'Coastal Carolina': {'SP_PLUS': -15.6, 'FPI': -13.9, 'ENTROPY': 32.69, 'MASSEY': 42.02},
                'Colorado': {'SP_PLUS': 1.7, 'FPI': 0.3, 'ENTROPY': 42.65, 'MASSEY': 54.09},
                'Colorado State': {'SP_PLUS': -12.8, 'FPI': -9.0, 'ENTROPY': 33.25, 'MASSEY': 44.92},
                'Connecticut': {'SP_PLUS': -24.7, 'FPI': -19.8, 'ENTROPY': 27.76, 'MASSEY': 33.86},
                'Duke': {'SP_PLUS': 2.9, 'FPI': 1.2, 'ENTROPY': 51.89, 'MASSEY': 66.03},
                'East Carolina': {'SP_PLUS': -14.4, 'FPI': -10.7, 'ENTROPY': 33.73, 'MASSEY': 42.45},
                'Eastern Michigan': {'SP_PLUS': -6.4, 'FPI': -11.5, 'ENTROPY': 35.34, 'MASSEY': 51.25},
                'Florida': {'SP_PLUS': 24.6, 'FPI': 17.6, 'ENTROPY': 64.8, 'MASSEY': 74.78},
                'Florida Atlantic': {'SP_PLUS': -1.3, 'FPI': -4.9, 'ENTROPY': 41.88, 'MASSEY': 52.49},
                'Florida International': {'SP_PLUS': -3.3, 'FPI': -2.4, 'ENTROPY': 39.76, 'MASSEY': 51.09},
                'Florida State': {'SP_PLUS': 10.9, 'FPI': 11.6, 'ENTROPY': 54.9, 'MASSEY': 59.84},
                'Fresno State': {'SP_PLUS': 5.5, 'FPI': -2.2, 'ENTROPY': 50.28, 'MASSEY': 67.86},
                'Georgia': {'SP_PLUS': 30.7, 'FPI': 22.3, 'ENTROPY': 72.19, 'MASSEY': 81.01},
                'Georgia Southern': {'SP_PLUS': -1.5, 'FPI': -3.1, 'ENTROPY': 44.95, 'MASSEY': 52.61},
                'Georgia State': {'SP_PLUS': -15.2, 'FPI': -12.1, 'ENTROPY': 29.89, 'MASSEY': 39.05},
                'Georgia Tech': {'SP_PLUS': -3.5, 'FPI': -4.6, 'ENTROPY': 47.06, 'MASSEY': 61.03},
                "Hawai'i": {'SP_PLUS': -5.5, 'FPI': -5.6, 'ENTROPY': 40.78, 'MASSEY': 46.24},
                'Houston': {'SP_PLUS': 0.3, 'FPI': -4.0, 'ENTROPY': 45.31, 'MASSEY': 53.46},
                'Illinois': {'SP_PLUS': -3.8, 'FPI': -3.9, 'ENTROPY': 41.64, 'MASSEY': 52.09},
                'Indiana': {'SP_PLUS': 6.4, 'FPI': 4.6, 'ENTROPY': 48.08, 'MASSEY': 59.74},
                'Iowa': {'SP_PLUS': 12.5, 'FPI': 10.5, 'ENTROPY': 56.1, 'MASSEY': 72.35},
                'Iowa State': {'SP_PLUS': 7.2, 'FPI': 9.8, 'ENTROPY': 54.53, 'MASSEY': 65.92},
                'Kansas': {'SP_PLUS': -12.1, 'FPI': -11.0, 'ENTROPY': 33.4, 'MASSEY': 53.58},
                'Kansas State': {'SP_PLUS': 3.0, 'FPI': 1.2, 'ENTROPY': 50.03, 'MASSEY': 62.25},
                'Kent State': {'SP_PLUS': -13.7, 'FPI': -13.8, 'ENTROPY': 30.08, 'MASSEY': 38.43},
                'Kentucky': {'SP_PLUS': 8.8, 'FPI': 6.3, 'ENTROPY': 51.93, 'MASSEY': 69.7},
                'Louisiana': {'SP_PLUS': -7.2, 'FPI': -8.6, 'ENTROPY': 38.59, 'MASSEY': 47.47},
                'Louisiana Monroe': {'SP_PLUS': -8.9, 'FPI': -9.2, 'ENTROPY': 36.23, 'MASSEY': 45.92},
                'Louisiana Tech': {'SP_PLUS': -2.4, 'FPI': -5.9, 'ENTROPY': 43.1, 'MASSEY': 49.44},
                'Louisville': {'SP_PLUS': -2.7, 'FPI': -1.0, 'ENTROPY': 44.44, 'MASSEY': 51.25},
                'LSU': {'SP_PLUS': 25.8, 'FPI': 21.7, 'ENTROPY': 69.46, 'MASSEY': 76.88},
                'Marshall': {'SP_PLUS': -1.2, 'FPI': -1.6, 'ENTROPY': 43.9, 'MASSEY': 54.9},
                'Maryland': {'SP_PLUS': 2.1, 'FPI': -1.3, 'ENTROPY': 40.23, 'MASSEY': 61.01},
                'Memphis': {'SP_PLUS': 12.3, 'FPI': 3.1, 'ENTROPY': 50.36, 'MASSEY': 58.38},
                'Miami': {'SP_PLUS': 13.9, 'FPI': 9.3, 'ENTROPY': 52.11, 'MASSEY': 63.26},
                'Miami (OH)': {'SP_PLUS': -4.9, 'FPI': -10.4,  'ENTROPY': 36.85, 'MASSEY': 53.45},
                'Michigan': {'SP_PLUS': 21.6, 'FPI': 21.2, 'ENTROPY': 65.45, 'MASSEY': 72.4},
                'Michigan State': {'SP_PLUS': 12.6, 'FPI': 14.0, 'ENTROPY': 60.42, 'MASSEY': 65.06},
                'Middle Tennessee': {'SP_PLUS': -9.3, 'FPI': -8.8, 'ENTROPY': 40.05, 'MASSEY': 54.19},
                'Minnesota': {'SP_PLUS': 9.5, 'FPI': 8.9, 'ENTROPY': 51.94, 'MASSEY': 65.01},
                'Mississippi State': {'SP_PLUS': 21.4, 'FPI': 13.7, 'ENTROPY': 60.42, 'MASSEY': 72.44},
                'Missouri': {'SP_PLUS': 17.5, 'FPI': 12.1, 'ENTROPY': 61.2, 'MASSEY': 70.77},
                'Navy': {'SP_PLUS': -16.3, 'FPI': -13.6, 'ENTROPY': 38.94, 'MASSEY': 50.37},
                'NC State': {'SP_PLUS': 6.3, 'FPI': 4.7, 'ENTROPY': 54.72, 'MASSEY': 65.78},
                'Nebraska': {'SP_PLUS': 6.6, 'FPI': 8.2, 'ENTROPY': 56.87, 'MASSEY': 62.72},
                'Nevada': {'SP_PLUS': -1.9, 'FPI': -8.8, 'ENTROPY': 41.78, 'MASSEY': 52.33},
                'New Mexico': {'SP_PLUS': -15.3, 'FPI': -13.4, 'ENTROPY': 31.76, 'MASSEY': 43.23},
                'North Carolina': {'SP_PLUS': 3.2, 'FPI': 2.3, 'ENTROPY': 44.11, 'MASSEY': 54.36},
                'Northern Illinois': {'SP_PLUS': -0.6, 'FPI': -8.0, 'ENTROPY': 42.57, 'MASSEY': 50.78},
                'North Texas': {'SP_PLUS': -2.0, 'FPI': -4.8, 'ENTROPY': 42.47, 'MASSEY': 49.81},
                'Northwestern': {'SP_PLUS': 4.2, 'FPI': 3.1, 'ENTROPY': 51.42, 'MASSEY': 67.89},
                'Notre Dame': {'SP_PLUS': 19.1, 'FPI': 18.2, 'ENTROPY': 64.98, 'MASSEY': 75.85},
                'Ohio': {'SP_PLUS': -1.9, 'FPI': -5.9, 'ENTROPY': 46.28, 'MASSEY': 58.23},
                'Ohio State': {'SP_PLUS': 24.3, 'FPI': 14.1, 'ENTROPY': 65.1, 'MASSEY': 76.15},
                'Oklahoma': {'SP_PLUS': 25.0, 'FPI': 19.6, 'ENTROPY': 68.77, 'MASSEY': 76.33},
                'Oklahoma State': {'SP_PLUS': 12.8, 'FPI': 7.1, 'ENTROPY': 55.71, 'MASSEY': 66.81},
                'Old Dominion': {'SP_PLUS': -17.6, 'FPI': -20.9, 'ENTROPY': 28.83, 'MASSEY': 39.49},
                'Ole Miss': {'SP_PLUS': 8.5, 'FPI': 6.1, 'ENTROPY': 52.31, 'MASSEY': 60.33},
                'Oregon': {'SP_PLUS': 13.8, 'FPI': 16.7, 'ENTROPY': 62.82, 'MASSEY': 62.94},
                'Oregon State': {'SP_PLUS': -9.4, 'FPI': -4.7, 'ENTROPY': 37.95, 'MASSEY': 45.35},
                'Penn State': {'SP_PLUS': 18.4, 'FPI': 15.6, 'ENTROPY': 60.52, 'MASSEY': 71.95},
                'Pittsburgh': {'SP_PLUS': 3.8, 'FPI': 4.0, 'ENTROPY': 50.11, 'MASSEY': 66.22},
                'Purdue': {'SP_PLUS': 4.2, 'FPI': 0.4, 'ENTROPY': 49.38, 'MASSEY': 65.22},
                'Rice': {'SP_PLUS': -20.0, 'FPI': -22.7, 'ENTROPY': 23.89, 'MASSEY': 32.63},
                'Rutgers': {'SP_PLUS': -12.3, 'FPI': -6.6, 'ENTROPY': 33.9, 'MASSEY': 48.72},
                'San Diego State': {'SP_PLUS': 4.9, 'FPI': -3.7, 'ENTROPY': 44.31, 'MASSEY': 51.59},
                'San José State': {'SP_PLUS': -16.2, 'FPI': -12.4, 'ENTROPY': 31.48, 'MASSEY': 42.39},
                'SMU': {'SP_PLUS': -2.2, 'FPI': -4.4, 'ENTROPY': 39.62, 'MASSEY': 48.51},
                'South Alabama': {'SP_PLUS': -20.8, 'FPI': -21.9, 'ENTROPY': 27.04, 'MASSEY': 38.24},
                'South Carolina': {'SP_PLUS': 14.9, 'FPI': 12.3, 'ENTROPY': 58.66, 'MASSEY': 65.86},
                'Southern Mississippi': {'SP_PLUS': 0.0, 'FPI': -3.0, 'ENTROPY': 42.91, 'MASSEY': 48.59},
                'South Florida': {'SP_PLUS': 1.0, 'FPI': -2.5, 'ENTROPY': 46.79, 'MASSEY': 48.04},
                'Stanford': {'SP_PLUS': 10.0, 'FPI': 7.6, 'ENTROPY': 56.6, 'MASSEY': 67.07},
                'Syracuse': {'SP_PLUS': 4.6, 'FPI': 3.9, 'ENTROPY': 52.93, 'MASSEY': 71.59},
                'TCU': {'SP_PLUS': 9.2, 'FPI': 7.5, 'ENTROPY': 56.22, 'MASSEY': 63.47},
                'Temple': {'SP_PLUS': 2.2, 'FPI': -3.2, 'ENTROPY': 45.04, 'MASSEY': 56.89},
                'Tennessee': {'SP_PLUS': 12.9, 'FPI': 14.0, 'ENTROPY': 53.9, 'MASSEY': 61.08},
                'Texas': {'SP_PLUS': 8.9, 'FPI': 10.0, 'ENTROPY': 58.91, 'MASSEY': 71.47},
                'Texas A&M': {'SP_PLUS': 18.7, 'FPI': 16.1, 'ENTROPY': 61.54, 'MASSEY': 74.21},
                'Texas State': {'SP_PLUS': -8.8, 'FPI': -11.5, 'ENTROPY': 25.67, 'MASSEY': 37.58},
                'Texas Tech': {'SP_PLUS': 4.8, 'FPI': 5.1, 'ENTROPY': 49.93, 'MASSEY': 61.7},
                'Toledo': {'SP_PLUS': -1.3, 'FPI': -3.4, 'ENTROPY': 45.03, 'MASSEY': 51.68},
                'Troy': {'SP_PLUS': 1.4, 'FPI': -6.7, 'ENTROPY': 40.7, 'MASSEY': 55.69},
                'Tulane': {'SP_PLUS': -7.2, 'FPI': -5.4, 'ENTROPY': 40.09, 'MASSEY': 53.45},
                'Tulsa': {'SP_PLUS': -6.0, 'FPI': -7.8, 'ENTROPY': 40.07, 'MASSEY': 44.56},
                'UAB': {'SP_PLUS': -9.8, 'FPI': -8.1, 'ENTROPY': 35.63, 'MASSEY': 54.14},
                'UCF': {'SP_PLUS': 11.7, 'FPI': 7.6, 'ENTROPY': 58.6, 'MASSEY': 69.61},
                'UCLA': {'SP_PLUS': 3.1, 'FPI': 11.9, 'ENTROPY': 51.34, 'MASSEY': 56.14},
                'UMass': {'SP_PLUS': -19.9, 'FPI': -18.3, 'ENTROPY': 26.46, 'MASSEY': 42.06},
                'UNLV': {'SP_PLUS': -7.5, 'FPI': -9.3, 'ENTROPY': 32.62, 'MASSEY': 44.31},
                'USC': {'SP_PLUS': 10.7, 'FPI': 10.0, 'ENTROPY': 54.4, 'MASSEY': 60.68},
                'Utah': {'SP_PLUS': 15.4, 'FPI': 11.5, 'ENTROPY': 59.06, 'MASSEY': 66.02},
                'Utah State': {'SP_PLUS': 7.6, 'FPI': -4.7, 'ENTROPY': 48.36, 'MASSEY': 63.78},
                'UTEP': {'SP_PLUS': -28.5, 'FPI': -22.0, 'ENTROPY': 20.36, 'MASSEY': 30.54},
                'UT San Antonio': {'SP_PLUS': -21.7, 'FPI': -14.5, 'ENTROPY': 27.88, 'MASSEY': 38.82},
                'Vanderbilt': {'SP_PLUS': 5.2, 'FPI': 3.8, 'ENTROPY': 49.3, 'MASSEY': 62.21},
                'Virginia': {'SP_PLUS': 7.9, 'FPI': 5.7, 'ENTROPY': 53.06, 'MASSEY': 64.32},
                'Virginia Tech': {'SP_PLUS': 10.6, 'FPI': 8.1, 'ENTROPY': 54.43, 'MASSEY': 58.55},
                'Wake Forest': {'SP_PLUS': 3.1, 'FPI': 0.6, 'ENTROPY': 47.17, 'MASSEY': 63.66},
                'Washington': {'SP_PLUS': 17.7, 'FPI': 13.5, 'ENTROPY': 58.55, 'MASSEY': 71.16},
                'Washington State': {'SP_PLUS': 8.9, 'FPI': 8.4, 'ENTROPY': 54.05, 'MASSEY': 68.04},
                'Western Kentucky': {'SP_PLUS': -8.6, 'FPI': -6.8, 'ENTROPY': 33.78, 'MASSEY': 42.54},
                'Western Michigan': {'SP_PLUS': -0.5, 'FPI': 0.4, 'ENTROPY': 43.43, 'MASSEY': 46.43},
                'West Virginia': {'SP_PLUS': 8.6, 'FPI': 1.1, 'ENTROPY': 53.15, 'MASSEY': 68.71},
                'Wisconsin': {'SP_PLUS': 20.1, 'FPI': 6.7, 'ENTROPY': 58.6, 'MASSEY': 69.12},
                'Wyoming': {'SP_PLUS': -4.7, 'FPI': -7.4, 'ENTROPY': 41.17, 'MASSEY': 53.49},
                'New Mexico State': {'SP_PLUS': -17.9, 'FPI': -17.8, 'ENTROPY': 27.03, 'MASSEY': 37.44},
                'Liberty': {'SP_PLUS': -13.8, 'FPI': -13.1, 'ENTROPY': 35.7, 'MASSEY': 41.13}}

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