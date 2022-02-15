import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
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


def generate_scaler():
    data_list = list()
    for key, value in data.items():
        data_list += value

    data_list = list(set(data_list))
    data_list = np.array(data_list)
    data_list = data_list.reshape(-1, 1)
    scaler = MinMaxScaler()
    scaler.fit(data_list)
    return scaler


def scale_data(scaler):
    data_np_arr_list = list()
    pprint(data)
    for key, value in data.items():
        data[key] = scaler.transform(np.array(value).reshape(-1, 1))
        data_np_arr_list += [item[0] for item in data[key].tolist()]
    pprint(sorted(data_np_arr_list, reverse=True))


    for key, value in data.items():
        plt.ylim((0, 0.001))
        plt.plot(value)
    plt.show()


if __name__ == '__main__':
    scaler = generate_scaler()
    scale_data(scaler)
