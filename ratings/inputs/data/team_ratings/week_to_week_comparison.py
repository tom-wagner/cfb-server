# from ratings.inputs.data.team_ratings.preseason import TEAM_RATINGS as TR_PRESEASON
from ratings.inputs.data.team_ratings.week_eight import TEAM_RATINGS as TR_WEEK_EIGHT
from ratings.inputs.data.team_ratings.week_seven import TEAM_RATINGS as TR_WEEK_SEVEN

diffs = {k: (sum(v.values()) - sum(TR_WEEK_EIGHT[k].values())) / 4 for k, v in TR_WEEK_SEVEN.items()}
filtered_diffs = {k: v for k, v in diffs.items() if abs(v) >= 2}

# check to see if week over week differences are reasonable
print(filtered_diffs)
