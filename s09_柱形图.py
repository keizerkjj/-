import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/bikeshare'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def get_chinese_font():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

def collect_analyze_data():
    mem_list = []
    cas_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file, delimiter=',',dtype='str',skiprows=1)
        duration_col = data_arr[:,0].reshape(-1, 1)
        member_col = data_arr[:,-1].reshape(-1, 1)
        du_mem_cols = np.concatenate([duration_col,member_col],axis=1)
        # 得到单个季度member平均骑行时间
        mem_arr = du_mem_cols[du_mem_cols[:,1] == 'Member']
        cas_arr = du_mem_cols[du_mem_cols[:,1] == 'Casual']

        mem_mean = np.mean(mem_arr[:,0].astype('float') / 1000 / 60)
        mem_list.append(mem_mean)
        cas_mean = np.mean(cas_arr[:,0].astype('float') / 1000 / 60)
        cas_list.append(cas_mean)
    return mem_list,cas_list

def visualize_data(mem_list,cas_list):
    bar_loc = np.arange(4)
    bar_width = 0.35
    scale_list = ['第{}季度'.format(i+1)for i in range(4)]

    plt.figure()
    plt.bar(bar_loc,mem_list,width=bar_width, color='g', alpha=0.7, label='会员')
    plt.bar(bar_loc + 0.35, cas_list, width=bar_width, color='r', alpha=0.7, label='非会员')
    plt.xticks(bar_loc + bar_width/2, scale_list, rotation=45,fontproperties=get_chinese_font())
    plt.title('成员季度平均骑行时间',fontproperties=get_chinese_font())
    plt.legend(loc = 'best',prop=get_chinese_font())
    plt.ylabel('平均骑行时间（单位：分钟）',fontproperties=get_chinese_font())
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'group_bar_chart.png'))
    plt.show()

def main():
    mem_list, cas_list = collect_analyze_data()
    visualize_data(mem_list,cas_list)


if __name__ == '__main__':
    main()
