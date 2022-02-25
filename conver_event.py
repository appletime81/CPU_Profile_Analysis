from datetime import datetime

event_list = [
    'ENTITY_UNUSED',
    'SS_RLC_DL_CMN',
    'SS_RLC_UL_CMN',
    'SS_RLC_DL_UE',
    'SS_RLC_UL_UE',
    'SS_MAC_DL_UE',
    'SS_MAC_UL_UE',
    'SS_CMN_TMR',
    'SS_CHNL_DECOMP_CMN',
    'SS_SCH_LVL1_CMN',
    'SS_SCH_LVL2_CMN',
    'SS_CL_CMN',
    'SS_DU_OAM_AGENT',
    'SS_DU_PM',
    'SS_DU_FM',
    'SS_DU_MGR',
    'SS_DU_RRM',
    'SS_DU_RRM_UE',
    'SS_APP_UE',
    'SS_F1AP',
    'SS_E2AP',
    'SS_SCTP',
    'SS_EGTP',
    'SS_UE_EGTP',
    'SS_NRUP',
    'SS_UDP',
    'SS_DU_NS_AGNT',
    'SS_DU_NS_SM_API_HDLR',
    'SS_MAX_ENTITY'
]


def convert_task(fileName):
    with open(f'{fileName}', 'r') as fp:
        lines = fp.readlines()
    new_lines = list()
    for line in lines:
        line_list = line.split(' ')
        line_list[0] = line_list[0].replace('\x1b[33m', '')
        try:
            line_list[3] = line_list[3].replace('\x1b[0m', '')
        except:
            pass
        try:
            if line_list[4] == 'p_task->msgHdr.srcEntType:' or line_list[4] == 'p_task->msgHdr.dstEntType:':
                line_list[-1] = event_list[int(line_list[-1].strip())] + '\n'
        except:
            pass
        new_lines.append(''.join(line_list))

    time_str = datetime.now().strftime('%Y%m%d_%H%M%S')
    with open(f'{fileName}_{time_str}.txt', 'w', encoding='utf-8') as fp:
        fp.writelines(new_lines)


if __name__ == '__main__':
    convert_task('run_20220225_log.txt')
