
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



slim_elements_df.to_csv('/Users/harryclements/Documents/GitHub/FPL-Dashboard/players_data.csv')









