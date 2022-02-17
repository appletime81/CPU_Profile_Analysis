import pandas as pd
import plotly.express as px

from pprint import pprint
from tokenize import String
from typing import List, Dict
from get_all_event import condition_option, get_all_events


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
            event_dict[event[1]].append(float(event[5]))
    return event_dict


def plot_bar(data: Dict):
    data_list = list()
    column_names = ['Period'] + [key for key, _ in data.items()]
    n = len(data.get(column_names[1]))

    for i in range(n):
        temp_list = [f'Period {i + 1}']
        temp_list += [value[i] for key, value in data.items()]
        data_list.append(temp_list)

    df = pd.DataFrame(data_list, columns=column_names)
    fig = px.bar(df, x='Period', y=column_names, barmode='group', color_discrete_sequence=px.colors.qualitative.Light24,
                 title='Time Statistics')

    # fig.write_html('temp.html')

    fig.show()


if __name__ == '__main__':
    file_name = 'MobaXterm_10.255.174.40_20220217_181140.txt'
    condition_list = condition_option('task_profile_info_ss_nrt_task')
    record_list, event_list = get_all_events(file_name, condition_list)
    event_dict = genTaskDict(event_list)
    event_dict = statsEvent(event_list, record_list, event_dict)
    plot_bar(event_dict)

    # print result
    pprint(event_dict)
