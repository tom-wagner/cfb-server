# from ratings.inputs.data.team_ratings.preseason import TEAM_RATINGS as TR_PRESEASON
from ratings.inputs.data.team_ratings.week_five import TEAM_RATINGS as TR_WEEK_FIVE
from ratings.inputs.data.team_ratings.week_six import TEAM_RATINGS as TR_WEEK_SIX

diffs = {k: (sum(v.values()) - sum(TR_WEEK_FIVE[k].values())) / 4 for k, v in TR_WEEK_SIX.items()}
filtered_diffs = {k: v for k, v in diffs.items() if abs(v) >= 3}

# check to see if week over week differences are reasonable
print(filtered_diffs)
