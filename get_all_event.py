from tokenize import String
from typing import List


def condition_option(opt_name: String):
    if opt_name == 'task_profile_info_ss_rt_task':
        task_profile_info_ss_rt_task = ['TASK PROFILE INFO', 'SS_RT_TASK', 'SS_NRT_TASK']
        return task_profile_info_ss_rt_task
    if opt_name == 'task_profile_info_ss_nrt_task':
        task_profile_info_ss_nrt_task = ['TASK PROFILE INFO', 'SS_NRT_TASK', 'QUEUE PROFILE INFO']
        return task_profile_info_ss_nrt_task


def get_all_events(txtFileName: String, condtion_list: List):
    # -------------------------declare vars-------------------------
    with open(txtFileName, 'r') as f:
        lines = f.readlines()
    event_list = list()
    ss_rt_or_nrt_flag = False
    start_record_flag = False
    record_list = list()
    n = len(lines)  # lines' length
    # --------------------------------------------------------------
    """
    1. get ss rt task from task profile info part
        - Condition 1:
            * String: 'TASK PROFILE INFO'
            * Bool Value: start_flag_record: True
        - Condition 2:
            * String: 'SS_RT_TASK'
            * Bool Value: ss_rt_or_nrt_flag: True
        - Condition 3:
            * String: 'SS_NRT_TASK'
            * Bool Value:  start_record_flag: False
                           ss_rt_or_nrt_flag: False
    2. get ss nrt task from task profile info part
        - Condition 1:
            * String: 'TASK PROFILE INFO'
            * Bool Value: start_flag_record: True
        - Condition 2:
            * String: 'SS_NRT_TASK'
            * Bool Value: ss_rt_or_nrt_flag: True
        - Condition 3:
            * String: 'QUEUE PROFILE INFO'
            * Bool Value:  start_record_flag: False
                           ss_rt_or_nrt_flag: False
    """
    for i in range(n):
        if condtion_list[0] in lines[i]:  # Condition1
            start_record_flag = True

        if condtion_list[1] in lines[i]:  # Condition2
            ss_rt_or_nrt_flag = True

        # if condtion_list[2] in lines[i]:  # Condition3
        #     if ss_rt_or_nrt_flag and start_record_flag:
        #         record_list.append('##########')
        #     start_record_flag = False
        #     ss_rt_or_nrt_flag = False

        if ss_rt_or_nrt_flag and start_record_flag and 'EVT_' not in lines[i]:
            if ss_rt_or_nrt_flag and start_record_flag:
                record_list.append('##########')
            start_record_flag = False
            ss_rt_or_nrt_flag = False

        if ss_rt_or_nrt_flag and start_record_flag:
            if 'EVT_' in lines[i]:
                temp_line = lines[i].replace(' ', '_')
                temp_line_list = temp_line.split('_')
                temp_line_list = [element for element in temp_line_list if element != '']
                temp_line_list = ['_'.join(temp_line_list[:4])] + ['_'.join(temp_line_list[4:-5])] + temp_line_list[-5:]
                record_list.append(temp_line_list)
                event_list.append(temp_line_list[1])

    event_list = list(set(event_list))
    return record_list, event_list
