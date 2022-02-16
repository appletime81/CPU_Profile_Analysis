from tokenize import String


def get_all_events(txtFileName: String):
    # -------------------------declare vars-------------------------
    with open(txtFileName, 'r') as f:
        lines = f.readlines()
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

    event_list = list(set(event_list))
    return record_list, event_list


if __name__ == '__main__':
    pass