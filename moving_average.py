# @author: ALI GHANBARI 
# @email: alighanbari446@gmail.com

import numpy as np
def moving_average(data_list, window_size):
    avg = 0
    a = np.array([])
    for i in range(len(data_list) - window_size + 1):
        avg = np.average(data_list[i:window_size+i])
        a = np.append(a, [avg])
    return a

data_list = np.array([1,5,3,4,4])
window_size = 3
moving_average(data_list, window_size)





