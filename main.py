import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import collections
from dash import Dash, html, dcc
from argparse import ArgumentParser
from pprint import pprint
from tokenize import String
from typing import List, Dict
from utils.get_all_event import condition_option, get_all_events
from utils.create_excel_stats_form import createExcelReport
from utils.convert_cycles_to_seconds import cpu_processing_time
from utils.color_dict import gen_color_dict

app = Dash(__name__)

FREQ = 1.3 * 1000


def readProfileFile(fileName: String):
    with open(fileName, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    return lines


def genTaskDict(event_names: List):
    return dict([(event_name, list()) for event_name in event_names])


def statsEvent(event_list: List, record_list: List, event_dict: Dict):
    temp_event_list = list()
    for event in record_list:
        if event == '##########':
            for element in event_list:
                if element not in temp_event_list:
                    event_dict[element].append(0)
            temp_event_list = list()
        else:
            temp_event_list.append(event[1])
            event_dict[event[1]].append(cpu_processing_time(float(event[4]), FREQ))
    return event_dict


def plot_bar(data: Dict, color_dict: Dict, fileName: String, option: String):
    def gen_chart_title(file_name: String, option: String):
        file_name_list = file_name.split('/')
        file_name = file_name_list[-1]
        cup_core, ue_per_tti, ue_nums = file_name.replace('.txt', '').split('-')[0:3]

        if 'queue' in option:
            if 'nrt' in option:
                return f'Non Real Time Task   |   In Queue   |   CPU核心數: {cup_core}   |   UE/TTI: {ue_per_tti}   |   UE個數: {ue_nums}'
            else:
                return f'Real Time Task   |   In Queue   |   CPU核心數: {cup_core}   |   UE/TTI: {ue_per_tti}   |   UE個數: {ue_nums}'
        else:
            if 'nrt' in option:
                return f'Non Real Time Task   |   Not In Queue   |   CPU核心數: {cup_core}   |   UE/TTI: {ue_per_tti}   |   UE個數: {ue_nums}'
            else:
                return f'Real Time Task   |   Not In Queue   |   CPU核心數: {cup_core}   |   UE/TTI: {ue_per_tti}   |   UE個數: {ue_nums}'

    title = gen_chart_title(file_name=fileName, option=option)

    sorted_data_key = sorted([key for key, _ in data.items()])
    new_data = dict([(key, data.get(key)) for key in sorted_data_key])

    data_list = list()
    column_names = ['Period'] + [key for key, _ in new_data.items()]
    n = len(data.get(column_names[1]))

    for i in range(n):
        temp_list = [f'Period {i + 1}']
        temp_list += [value[i] for key, value in new_data.items()]
        data_list.append(temp_list)

    df = pd.DataFrame(data_list, columns=column_names)

    # ------------ plot chart ------------

    # fig = px.bar(df, x='Period', y=column_names, barmode='group', color_discrete_sequence=px.colors.qualitative.Light24,
    #              title='Time Statistics')
    # fig.write_html('temp.html')
    fig = go.Figure()
    for column_name in column_names:
        if column_name != 'Period':
            fig.add_trace(
                go.Bar(
                    x=df['Period'].to_list(),
                    y=df[column_name].to_list(),
                    name=column_name,
                    marker_color=color_dict.get(column_name)
                )
            )
    fig.update_layout(
        title=title,
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='秒數',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=1.0,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1,  # gap between bars of the same location coordinate.
        hoverlabel_namelength=50,
        width=1691,
        height=940
    )
    fig.update_yaxes(
        range=[0, 1]
    )
    return fig


def plot_bar_with_sns(data: Dict):
    data_list = list()
    new_data_list = list()
    for k, v in data.items():
        data_list.append([[k, item] for item in v])

    for i in range(len(data_list[0])):
        for j in range(len(data_list)):
            new_data_list.append(data_list[j][i])

    period_list = [[i + 1] * 12 for i in range(21)]
    new_period_list = list()

    for sub_list in period_list:
        for num in sub_list:
            new_period_list.append(num)

    data_dict = {
        'Period': new_period_list,
        'Event': [item[0] for item in new_data_list],
        'Time': [item[1] for item in new_data_list],

    }
    df = pd.DataFrame(data_dict)

    sns.barplot(x='Period', y='Time', hue='Event', data=df)
    plt.show()


if __name__ == '__main__':
    # UE_NUMS, POOL_NUMS, UR_PER_TTI
    parser = ArgumentParser()
    parser.add_argument('--option', default='queue_profile_info_ss_nrt_task',
                        help='Search Task Profile Info Content or Queue Profile Info')
    parser.add_argument('--f', default='0225/frank/2-1-1.txt', help='file name')
    parser.add_argument('--ue', default='32', help='UE Numbers')
    parser.add_argument('--pool', default='1', help='Pool Numbers')
    parser.add_argument('--uetti', default='1', help='UE Per TTI')

    args = parser.parse_args()
    file_name = args.f
    ue_nums = args.ue
    pool_nums = args.pool
    ue_per_tti = args.uetti
    option = args.option

    condition_list = condition_option(option)
    record_list, event_list = get_all_events(file_name, condition_list)
    # createExcelReport(record_list, event_list, option, ue_nums, pool_nums, ue_per_tti)

    # ----------------------------------------------------------------------
    event_dict = genTaskDict(event_list)
    event_dict = statsEvent(event_list, record_list, event_dict)
    color_dict = gen_color_dict()
    pprint(color_dict)
    fig = plot_bar(event_dict, color_dict, file_name, option)
    fig.show()
    fig.write_html(f'analysis_result/{option}_{file_name.split("/")[-1].replace(".txt", "").replace("-", "_")}.html')

    # -------------- dash server --------------
    # app.layout = html.Div(children=[
    #     html.Title(children='21212'),
    #     html.H1(children='Hello Dash'),
    #
    #     html.Div(children='''
    #         Dash: A web application framework for your data.
    #     '''),
    #
    #     dcc.Graph(
    #         id='example-graph',
    #         figure=fig
    #     )
    # ])
    # app.title = f'{file_name.split("/")[-1].replace(".txt", "")}_{option}'
    # app.run_server(debug=True)
