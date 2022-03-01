import cv2
import matplotlib.cm as cm
import numpy as np

from datetime import datetime
from pprint import pprint


def gen_zeros():
    return np.zeros((100, 100, 3))


def gen_random_color():
    num_classes = 60
    cmap = cm.rainbow(np.linspace(0.0, 1.0, num_classes))

    color_list = list()
    for i in range(len(cmap)):
        for j in range(len(cmap[i])):
            cmap[i][j] = cmap[i][j] * 256

    for i in range(len(cmap)):
        # color_list.append((np.array(cmap[i][0]).astype(np.uint8),
        #                    np.array(cmap[i][1]).astype(np.uint8),
        #                    np.array(cmap[i][2]).astype(np.uint8)))

        color_list.append(f'rgb({np.array(cmap[i][0]).astype(np.uint8)}, {np.array(cmap[i][1]).astype(np.uint8)}, {np.array(cmap[i][2]).astype(np.uint8)})')

    # pprint(color_list)
    return color_list


if __name__ == '__main__':
    # num_classes = 60
    # cmap = cm.rainbow(np.linspace(0.0, 1.0, num_classes))
    # print(cmap)
    #
    # for i in range(len(cmap)):
    #     for j in range(len(cmap[i])):
    #         cmap[i][j] = cmap[i][j] * 256
    #
    # colors = list()
    # for i in range(59):
    #     colors.append(gen_zeros())
    #
    # for i in range(len(colors)):
    #     colors[i][:, :, 0] = cmap[i][0]
    #     colors[i][:, :, 1] = cmap[i][1]
    #     colors[i][:, :, 2] = cmap[i][2]
    #     colors[i] = colors[i].astype(np.uint8)
    #
    # all_colors = colors[0]
    # for i, color in enumerate(colors):
    #     if i > 0:
    #         all_colors = np.concatenate((all_colors, color), axis=0)
    #
    # cv2.imwrite(f'{datetime.now().strftime("%Y%m%d_%H%M%S")}_color.png', all_colors)
    pprint(gen_random_color())