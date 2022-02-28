from pprint import pprint

"""
# SS_RT_EVT
- EVT_TFU_RA_REQUEST_INDICATION
- EVT_TFU_CRC_INDICATION
- EVT_UDX_STA_PHBT_START_TIMER
- EVT_L1_MSG_INDICATION
- EVT_COMMON_UE_ACK_INDICATION
- EVT_RGR_LVL1_CONFIG_REQUEST
- EVT_CTF_CONFIG_REQUEST
- EVT_KW_UMUL_REASSEMBLE_TIMER
- EVT_RGR_LVL2_CONFIG_REQUEST
- EVT_KW_AMUL_STA_PROH_TIMER
- EVT_RGR_LVL1_CCCH_DATA_REQUEST
- EVT_RGR_LVL1_SI_CONFIG_REQUEST
- EVT_COMMON_UE_ACK_INDICATION



"""



def stats_all_events(fileName):
    with open(f'{fileName}', 'r') as fp:
        lines = fp.readlines()
    all_events = list(set(lines))
    for i in range(len(all_events)):
        print(all_events[i].strip())


if __name__ == '__main__':
    fille_name = '所有事件.txt'
    stats_all_events(fileName=fille_name)
