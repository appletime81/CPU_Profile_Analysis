import pandas as pd
import plotly.express as px

from pprint import pprint
from tokenize import String
from typing import List, Dict


def readProfileFile(fileName: String):
    with open(fileName, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    return lines


def analysisTextContent(lines: List):
    # -------------------------declare vars-------------------------
    event_list = list()
    ss_rt_flag = False
    start_record_flag = False
    record_list = list()
    n = len(lines)  # lines' length
    # --------------------------------------------------------------

    for i in range(n):
        if 'QUEUE PROFILE INFO' in lines[i]:
            start_record_flag = True

        if 'SS_RT_TASK' in lines[i]:
            ss_rt_flag = True

        if 'SS_NRT_TASK' in lines[i]:
            start_record_flag = False
            ss_rt_flag = False

        if ss_rt_flag and start_record_flag:
            if 'EVT_' in lines[i]:
                temp_line = lines[i].replace(' ', '_')
                temp_line_list = temp_line.split('_')
                temp_line_list = [element for element in temp_line_list if element != '']
                temp_line_list = ['_'.join(temp_line_list[:4])] + ['_'.join(temp_line_list[4:-4])] + temp_line_list[-4:]
                record_list.append(temp_line_list)
                event_list.append(temp_line_list[1])
    event_list = list(set(event_list))
    pprint(event_list)
    return record_list, event_list


def statisticsEveryEventTime(events: List, event_names: List):
    ss_rt_events = event_names
    ss_rt_task = dict([(element, list()) for element in ss_rt_events])

    for event in events:
        ss_rt_task[event[1]].append(float(event[4]))

    return ss_rt_task


def plot_hist(data: Dict):
    data_list = list()
    column_names = ['Period'] + [key for key, _ in data.items()]
    for key, value in data.items():
        if len(value) < 8:
            data[key] = value + [0] * (8 - len(value))

    for i in range(8):
        temp_list = [f'Period {i + 1}']
        temp_list += [value[i] for key, value in data.items()]
        data_list.append(temp_list)

    df = pd.DataFrame(data_list, columns=column_names)
    px.bar(df, x='Period', y=column_names, barmode='group', color_discrete_sequence=px.colors.qualitative.Light24,
           title='Time Statistics').show()


if __name__ == '__main__':
    lines = readProfileFile('2 core/MobaXterm_10.255.174.35_20220216_163442.txt')
    record_list, event_names = analysisTextContent(lines)
    ss_rt_task = statisticsEveryEventTime(record_list, event_names)
    plot_hist(ss_rt_task)
    # pprint(ss_rt_task)
