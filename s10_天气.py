import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/temp2.csv'

data_arr = np.loadtxt(data_path, delimiter=',', skiprows=1)
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)
month_list = [1,2,3]
scale_list = ['第{}月'.format(i+1)for i in range(3)]
bar_loc = np.arange(3)
bar_width = 0.35
positive_temp = []
negative_temp = []


def get_chinese_font():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

for month in month_list:
    mon_arr = data_arr[data_arr[:,0] == month]
    # 利用shape[0]得到arr的统计数量
    zero_up = mon_arr[mon_arr[:,1] >= 0].shape[0]
    zero_down = mon_arr[mon_arr[:,1] < 0].shape[0]
    positive_temp.append(zero_up)
    negative_temp.append(zero_down)

# 在利用matplotlib前，前面需要返回一个被分析过的list，要么是shape统计数量，要么是mean之类的
plt.figure()
plt.bar(bar_loc, positive_temp, width=bar_width, color='g', alpha=0.7, label='零上')
plt.bar(bar_loc + 0.35, negative_temp, width=bar_width, color='r', alpha=0.7, label='零下')
plt.xticks(bar_loc+ bar_width/2, scale_list, rotation=45,fontproperties=get_chinese_font())
plt.legend(loc = 'best',prop=get_chinese_font())
plt.title('温度分布',fontproperties=get_chinese_font())
plt.savefig(os.path.join(output_path, 'wea_bar.png'))
plt.show()