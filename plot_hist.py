import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

from pprint import pprint

data = {'EVT_COMMON_UE_ACK_INDICATION': [1602.0, 1602.0, 1602.0],
        'EVT_CTF_CONFIG_REQUEST': [461810.0,
                                   461810.0,
                                   461810.0,
                                   461810.0,
                                   461810.0,
                                   461810.0,
                                   461810.0,
                                   461810.0],
        'EVT_KW_AMUL_STA_PROH_TIMER': [290.0, 1592.0, 1592.0, 1592.0],
        'EVT_L1_MSG_INDICATION': [13402.0,
                                  12724.0,
                                  12962.0,
                                  12412.0,
                                  17248.0,
                                  18040.0,
                                  15298.0,
                                  16954.0],
        'EVT_RGR_LVL1_CCCH_DATA_REQUEST': [1906.0, 1906.0, 1906.0, 1906.0],
        'EVT_RGR_LVL1_CONFIG_REQUEST': [2081182.0,
                                        2081182.0,
                                        2081182.0,
                                        2081182.0,
                                        13178.0,
                                        6664.0,
                                        6664.0,
                                        6664.0],
        'EVT_RGR_LVL1_SI_CONFIG_REQUEST': [5224.0,
                                           5224.0,
                                           5224.0,
                                           5224.0,
                                           5224.0,
                                           5224.0,
                                           5224.0,
                                           5224.0],
        'EVT_RGR_LVL2_CONFIG_REQUEST': [19000.0,
                                        19000.0,
                                        19000.0,
                                        19000.0,
                                        19000.0,
                                        19000.0,
                                        19000.0,
                                        19000.0],
        'EVT_TFU_CRC_INDICATION': [3270.0, 3342.0, 3342.0, 3342.0],
        'EVT_TFU_RA_REQUEST_INDICATION': [32238.0, 32238.0, 32238.0, 32238.0],
        'EVT_UDX_STA_PHBT_START_TIMER': [1590.0, 2318.0, 2318.0, 2318.0]}


def plot_hist():
    data_list = list()
    column_names = ['Period'] + [key for key, _ in data.items()]
    for key, value in data.items():
        if len(value) < 8:
            data[key] = value + [0] * (8 - len(value))

    for i in range(8):
        temp_list = [f'Period {i + 1}']
        temp_list += [value[i] for key, value in data.items()]
        data_list.append(temp_list)

    pprint(data_list)
    df = pd.DataFrame(data_list, columns=column_names)
    px.bar(df, x='Period', y=column_names, barmode='group', title='Time Statistics').show()


plot_hist()
