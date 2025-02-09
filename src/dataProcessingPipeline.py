
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)
json = r.json()

# print(json.keys())

elements_df = pd.DataFrame(json['elements'])
elements_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])

# print(elements_df.head())
# print(elements_df.columns)


slim_elements_df = elements_df[['second_name', 'team', 'element_type', 'selected_by_percent', 'now_cost',
                                'minutes', 'transfers_in', 'value_season', 'total_points']]
# print(slim_elements_df.head())


slim_elements_df




slim_elements_df['position'] = slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)
# print(slim_elements_df.head())

slim_elements_df['team'] = slim_elements_df.team.map(teams_df.set_index('id').name)
slim_elements_df['value'] = slim_elements_df.value_season.astype(float)
# print(slim_elements_df.sort_values('value', ascending = False).head(10))





slim_elements_df.pivot_table(index = 'position', values = 'value', aggfunc = np.mean).reset_index()

pivot = slim_elements_df.pivot_table(index = 'position', values = 'value', aggfunc = np.mean).reset_index()
# print(pivot.sort_values('value', ascending = False))

slim_elements_df = slim_elements_df.loc[slim_elements_df.value > 0]

pivot = slim_elements_df.pivot_table(index = 'position', values = 'value', aggfunc = np.mean).reset_index()
# print(pivot.sort_values('value', ascending = False))

team_pivot = slim_elements_df.pivot_table(index = 'team', values = 'value', aggfunc = np.mean).reset_index()
# print(team_pivot.sort_values('value', ascending = False))



slim_elements_df.to_csv('./players_data.csv')



# Second more comprehensive dataframe to use


# Get teams
teams_df = pd.DataFrame(json['teams'])
# Get players
elements_df = pd.DataFrame(json['elements'])
# Get links to positions etc.
element_stats_df = pd.DataFrame(json['element_stats'])
element_types_df = pd.DataFrame(json['element_types'])

# Combine all of the dataframes to get the positions and teams
combined_team_df = elements_df.merge(teams_df, left_on = "team", right_on = "id", how = "left")
combined_team_position_df = combined_team_df.merge(element_types_df, left_on = "element_type", right_on = "id")

# Have a quick look at the shape of the dataframe
combined_team_position_df.shape

# Filter out players who don't have any points
players_with_points = combined_team_position_df[combined_team_position_df["total_points"] != 0]



columns_for_investigation = ["web_name", "name", "singular_name", "now_cost", "total_points", "influence", "creativity", "threat", "ict_index",
                             "clean_sheets", "expected_goals", "expected_assists", "expected_goal_involvements",
                               "expected_goals_conceded", "expected_goals_per_90", "expected_assists_per_90",
                                 "expected_goal_involvements_per_90", "expected_goals_conceded_per_90", "goals_conceded_per_90",
                                 "starts_per_90", "clean_sheets_per_90"]


plotting_data = players_with_points.loc[:, columns_for_investigation]

for i in columns_for_investigation[3:]:
    plotting_data[i] = plotting_data[i].astype(float)


plotting_data.to_csv("./comprehensive_players_data.csv")




