import pandas as pd
from typing import Dict
from pprint import pprint


def save_event_to_csv(data: Dict):
    for k, v in data.items():
        if k == 'Real Time Event':
            real_time_event = v
        else:
            non_real_time_event = v

    real_time_event = sorted(real_time_event)
    non_real_time_event = sorted(non_real_time_event)

    diff_len_num = len(non_real_time_event) - len(real_time_event)
    real_time_event = real_time_event + [' '] * diff_len_num

    data = {
        "Real Time Event": real_time_event,
        "Non Real Time": non_real_time_event
    }

    df = pd.DataFrame(data)
    df.to_csv('事件分類.csv', index=False)


if __name__ == '__main__':
    data = {
        'Real Time Event': [
            "EVT_TFU_RA_REQUEST_INDICATION",
            "EVT_RGR_LVL1_CCCH_DATA_REQUEST",
            "EVT_RGR_LVL1_SI_CONFIG_REQUEST",
            "EVT_RGR_LVL1_CONFIG_REQUEST",
            "EVT_L1_MSG_INDICATION",
            "EVT_CTF_CONFIG_REQUEST",
            "EVT_KW_UMUL_REASSEMBLE_TIMER",
            "EVT_RGR_LVL2_CONFIG_REQUEST",
            "EVT_UDX_STA_PHBT_START_TIMER",
            "EVT_TFU_CRC_INDICATION",
            "EVT_COMMON_UE_ACK_INDICATION",
            "EVT_KW_AMUL_STA_PROH_TIMER"
        ],
        "Non Real Time": [
            "EVT_UDX_STA_UPD_REQUEST",
            "EVT_KWU_DATA_INDICATION",
            "EVT_EGTP_TTI_INDICATION",
            "EVT_RRM_UE_RECONFIG_RESPONSE",
            "EVT_OAM_CELL_CONFIG_REQUEST",
            "EVT_UDX_STA_PDU_REQUEST",
            "EVT_SCTP_CONFIG_REQUEST",
            "EVT_F1AP_UE_ID_RESPONSE",
            "EVT_NRUP_ADD_RAB_RESPONSE",
            "EVT_CTF_CONFIG_CONFIRM",
            "EVT_EGTP_ADD_TUNNEL_REQUEST",
            "EVT_UDX_CONFIG_CONFIRM",
            "EVT_RLC_FLW_CTRL_INFO_INDICATION",
            "EVT_RGR_LVL1_CONFIG_CONFIRM",
            "EVT_F1AP_UE_MSG_RX",
            "EVT_F1AP_UE_ID_REQUEST",
            "EVT_TIMER_TICK_INDICATION",
            "EVT_F1AP_MGMT_MSG_TX",
            "EVT_F1AP_MGMT_MSG_RX",
            "EVT_NRUP_EGTPU_DATA_INDICATION",
            "EVT_SCTP_USER_PAYLOAD_INDICATION",
            "EVT_RLC_UE_CONFIG_CONFIRM",
            "EVT_SCTP_CONFIG_RESPONSE",
            "EVT_RGR_LVL2_CONFIG_CONFIRM",
            "EVT_RGR_LVL1_SI_CONFIG_CONFIRM",
            "EVT_RGR_LVL1_CCCH_DATA_INDICATION",
            "EVT_RLC_REQ_FLW_CTRL_INFO",
            "EVT_RRM_CELL_ADD_REQUEST",
            "EVT_RRM_UE_RECONFIG_REQUEST",
            "EVT_UDX_DL_CLEANUP_MEM",
            "EVT_EGTP_ADD_TUNNEL_RESPONSE",
            "EVT_RRM_UE_ADMIT_CONFIRM",
            "EVT_APP_LCL_CELL_ADD_REQ",
            "EVT_KWU_DATA_REQUEST",
            "EVT_UDX_CONFIG_REQUEST",
            "EVT_SCTP_ASSOC_STATUS",
            "EVT_APP_UE_RRC_RECONFIG_DELIVERY_INDICATION",
            "EVT_APP_LCL_CELL_ADD_RSP",
            "EVT_OAM_DU_CONFIG_REQUEST",
            "EVT_RRM_UE_ADMIT_REQUEST",
            "EVT_RGR_LVL1_TTI_INDICATION",
            "EVT_SCTP_USER_PAYLOAD_REQUEST",
            "EVT_EGTP_INIT_REQUEST",
            "EVT_NRUP_ADD_RAB_REQUEST",
            "EVT_F1AP_UE_MSG_TX",
            "EVT_RRM_CELL_ADD_CONFIRM",
            "EVT_CKW_UL_CONFIG_REQUEST"
        ]
    }
    save_event_to_csv(data)
