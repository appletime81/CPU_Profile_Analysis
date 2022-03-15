import streamlit as st
import pandas as pd
import numpy as np
from pprint import pprint
import plotly.express as px

df = pd.read_csv('task_profile_info_ss_nrt_task_3_1_1.csv')
col_names = df.columns
N = len(df[col_names[0]])
print(N)

data_dict = {
    "Period": [],
    "Event": [],
    "AVG_CYCLES": []
}
for col_name in col_names:
    for i in range(N):
        data_dict['Period'].append(i + 1)
        data_dict['Event'].append(col_name)
        data_dict['AVG_CYCLES'].append(df.loc[i, (col_name)])

new_df = pd.DataFrame(data_dict)
new_df = new_df.sort_values(by=['Period'])
new_df.to_csv('test.csv', index=False)

fig = px.bar(new_df, x='Period', y='AVG_CYCLES', color='Event')
fig.update_layout(barmode='group')
fig.show()


# df = px.data.gapminder().query("continent == 'Oceania'")
# print(df)
