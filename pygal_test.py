import pygal
import pandas as pd

df = pd.read_csv('analysis_result_for_execution_times/task_profile_info_ss_nrt_task_3_1_16.csv')
col_names = df.columns

bar_chart = pygal.Bar(width=1000, height=1000)
bar_chart.title = 'Test'
for col_name in col_names:
    bar_chart.add(col_name, df[col_name].to_list())



# bar_chart = pygal.Bar(width=1000, height=1000)
# bar_chart.title = 'Browser usage evolution (in %)'
# bar_chart.x_labels = map(str, range(2002, 2013))
# bar_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
# bar_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
# bar_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
# bar_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
# bar_chart.y_labels= [str(i * 10) for i in range(5)]
bar_chart.render_in_browser()