
import numpy as np
import matplotlib.pyplot as plt

data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/temp2.csv'

time_in_min_com = []
data_arr = np.loadtxt(data_path, delimiter=',', skiprows=1)
# 注意，上面的dtype应该去掉
for month in range(1,4):
    bool_col = data_arr[:, 0] == month
    #利用bool来选择对应月份的数据
    temp_col = data_arr[bool_col]
    temp_max = np.max(temp_col)
    temp_min = np.min(temp_col)
    mean_tem = np.mean(temp_col)
    print('第{}月的最大值是{:.2f},最小值是{:.2f},平均数是{:.2f}'.format(month,temp_max,temp_min,mean_tem))

