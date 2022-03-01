import numpy as np
import matplotlib.pyplot as plt
import cv2


def random_give_rgb_color():
    r = np.random.randint(0, 256, 59)
    g = np.random.randint(0, 256, 59)
    b = np.random.randint(0, 256, 59)
    return r, g, b


if __name__ == "__main__":
    print('I am here')
    color_list = list()
    r, g, b = random_give_rgb_color()
    print(r[0])
    print("sdfs")
    for i in range(59):
        color_list.append(str(r[i]) + str(g[i]) + str(b[i]))
    set_color = set(color_list)
    print(len(set_color))
