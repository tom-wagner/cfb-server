# from ratings.inputs.data.team_ratings.preseason import TEAM_RATINGS as TR_PRESEASON
from ratings.inputs.data.team_ratings.week_thirteen import TEAM_RATINGS as TR_WEEK_TW
from ratings.inputs.data.team_ratings.week_fourteen import TEAM_RATINGS as TR_WEEK_FOURTEEN

diffs = {k: (sum(v.values()) - sum(TR_WEEK_FOURTEEN[k].values())) / 4 for k, v in TR_WEEK_TW.items()}
filtered_diffs = {k: v for k, v in diffs.items() if abs(v) >= 2}

# check to see if week over week differences are reasonable
print(filtered_diffs)
