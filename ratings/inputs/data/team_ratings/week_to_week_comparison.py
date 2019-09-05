from ratings.inputs.data.team_ratings.preseason import TEAM_RATINGS as TR_PRESEASON
from ratings.inputs.data.team_ratings.week_one import TEAM_RATINGS as TR_WEEK_ONE

diffs = {k: (sum(v.values()) - sum(TR_PRESEASON[k].values())) / 4 for k, v in TR_WEEK_ONE.items()}
filtered_diffs = {k: v for k, v in diffs.items() if v >= 3}

# check to see if week over week differences are reasonable
print(filtered_diffs)

