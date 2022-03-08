import numpy as np
from pprint import pprint

def test_func(data):
    test_lst = list()
    for k, v in data.items():
        test_lst.append(v)

    test_ary = np.array(test_lst)
    test_ary_sum = np.sum(test_ary, axis=1)
    pprint(test_ary)
    pprint(np.sum(test_ary, axis=1))
    print(type(np.max(test_ary_sum)))


if __name__ == '__main__':
    a = {
        'a': [1, 2, 3],
        'b': [1, 2, 3],
        'c': [4, 5, 6]
    }
    test_func(a)
    print('fsdsf', end=': ')
    print('sdfsd', end='')
    print(11)
