import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from pprint import pprint

sns.set_theme()

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

    colors = [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765),
              (1.0, 0.4980392156862745, 0.054901960784313725),
              (0.17254901960784313, 0.6274509803921569, 0.17254901960784313),
              (0.8392156862745098, 0.15294117647058825, 0.1568627450980392),
              (0.5803921568627451, 0.403921568627451, 0.7411764705882353),
              (0.5490196078431373, 0.33725490196078434, 0.29411764705882354),
              (0.8901960784313725, 0.4666666666666667, 0.7607843137254902),
              (0.4980392156862745, 0.4980392156862745, 0.4980392156862745),
              (0.7372549019607844, 0.7411764705882353, 0.13333333333333333),
              (0.09019607843137255, 0.7450980392156863, 0.8117647058823529),
              (0, 0, 0)]

    print(f'len(data) = {len(data)}')
    i = 0
    for key, value in data.items():
        plt.ylim((0, 0.02))
        print(colors[i])
        plt.plot(value, color=colors[i])
        i += 1
    plt.show()


if __name__ == '__main__':
    scaler = generate_scaler()
    scale_data(scaler)
