from tokenize import String
from typing import List

import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint


def readProfileFile(fileName: String):
    with open(fileName, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    # pprint(lines)
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
        if 'TASK PROFILE INFO' in lines[i]:
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
                temp_line_list = ['_'.join(temp_line_list[:4])] + ['_'.join(temp_line_list[4:-5])] + temp_line_list[-5:]
                record_list.append(temp_line_list)
                event_list.append(temp_line_list[1])

    # event_list = list(set(event_list))
    # print('------------------- EVT LIST -------------------')
    # pprint(event_list)

    return record_list


def statisticsEveryEventTime(events: List):
    ss_rt_events = ['EVT_RGR_LVL2_CONFIG_REQUEST',
                    'EVT_TFU_RA_REQUEST_INDICATION',
                    'EVT_L1_MSG_INDICATION',
                    'EVT_KW_AMUL_STA_PROH_TIMER',
                    'EVT_COMMON_UE_ACK_INDICATION',
                    'EVT_TFU_CRC_INDICATION',
                    'EVT_UDX_STA_PHBT_START_TIMER',
                    'EVT_CTF_CONFIG_REQUEST',
                    'EVT_RGR_LVL1_SI_CONFIG_REQUEST',
                    'EVT_RGR_LVL1_CCCH_DATA_REQUEST',
                    'EVT_RGR_LVL1_CONFIG_REQUEST']
    ss_rt_task = dict([(element, list()) for element in ss_rt_events])

    for event in events:
        ss_rt_task[event[1]].append(float(event[5]))

    return ss_rt_task


if __name__ == '__main__':
    lines = readProfileFile('no_traffic.txt')
    record_list = analysisTextContent(lines)
    ss_rt_task = statisticsEveryEventTime(record_list)
    pprint(ss_rt_task)

    for key, value in ss_rt_task.items():
        print(len(value))
