import pandas as pd
import plotly.express as px
import collections
from argparse import ArgumentParser
from pprint import pprint
from tokenize import String
from typing import List, Dict
from utils.get_all_event import condition_option, get_all_events
from utils.create_excel_stats_form import createExcelReport
from utils.convert_cycles_to_seconds import cpu_processing_time

FREQ = 1.3 * 1000


def readProfileFile(fileName: String):
    with open(fileName, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    return lines


def genTaskDict(event_names: List):
    return dict([(event_name, list()) for event_name in event_names])


def statsEvent(event_list: List, record_list: List, event_dict: Dict):
    temp_event_list = list()
    # pprint(record_list)
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


def plot_bar(data: Dict):
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
    fig = px.bar(df, x='Period', y=column_names, barmode='group', color_discrete_sequence=px.colors.qualitative.Light24,
                 title='Time Statistics')
    # fig.write_html('temp.html')
    fig.show()


if __name__ == '__main__':
    # UE_NUMS, POOL_NUMS, UR_PER_TTI
    parser = ArgumentParser()
    parser.add_argument('--option', default='queue_profile_info_ss_rt_task',
                        help='Search Task Profile Info Content or Queue Profile Info')
    parser.add_argument('--f', default='0225/frank/2-4-32.txt', help='file name')
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
    plot_bar(event_dict)

    # print result
    # pprint(event_dict)

    # od = dict(collections.OrderedDict(sorted(event_dict.items(), key=lambda x: x[1][-1], reverse=True)))
    # print(od)
