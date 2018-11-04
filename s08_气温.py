import os
import numpy as np
import matplotlib.pyplot as plt


data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/temp2.csv'
time_in_min_com = []
data_arr = np.loadtxt(data_path, delimiter=',', skiprows=1)
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

temp_hist,temp_bins = np.histogram(data_arr[:,1], range=(-10,10), bins= 10)
print(f'温度直方图的信息是:{temp_hist},边界是：{temp_bins}')

plt.figure(figsize=(10,5))
plt.hist(data_arr[:,1],range=(-10,10), bins= 10)
plt.xticks(temp_bins)
plt.title('Temp distribution')
plt.savefig(os.path.join(output_path, 'wea_histogram.png'))
plt.show()