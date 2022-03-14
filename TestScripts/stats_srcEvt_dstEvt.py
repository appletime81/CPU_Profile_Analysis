def stats_srcEvt_dstEvt(fileName):
    with open(fileName, 'r') as fp:
        lines = fp.readlines()

    stats_list = list()
    for i, line in enumerate(lines):
        if 'p_task->msgHdr' in line and 'SS_' in line and 'SS_' in lines[i + 1]:
            stats_list.append([line, lines[i + 1]])

    new_stats_list = list()
    for info in stats_list:
        new_stats_list.append(
            (info[0].replace('gnb_du_1|', '').strip() + ' ' + info[1].replace('gnb_du_1|', '').strip())
        )

    new_stats_dict = dict()
    for item in new_stats_list:
        if item not in new_stats_dict:
            new_stats_dict[item] = 1
        new_stats_dict[item] += 1

    print(new_stats_dict)


if __name__ == '__main__':
    fileName = 'run_20220225_log.txt_20220225_173616.txt'
    stats_srcEvt_dstEvt(fileName)
