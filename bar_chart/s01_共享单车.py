import os
import numpy as np
import matplotlib.pyplot as plt

data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/bikeshare'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']
def collect_data():
    data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)
        data_arr_list.append(data_arr)
    return data_arr_list

def process_data(data_arr_list):
    time_in_min_com = []
    for data_arr in data_arr_list:
        duration_col = data_arr[:,0] # ":"表示选取所有，"0"表示第一行
        # 开始转换数据类型
        #time_in_ms = np.core.defchararray.replace(duration_col,'"','')
        time_in_min = duration_col.astype('float')/1000/60
        time_in_min_com.append(time_in_min)
    return time_in_min_com

def analyze_data(time_in_min_com):
    time_mean_list = []
    # 利用for循环来遍历list里面的index和对应的数值
    for index,time in enumerate(time_in_min_com):
        time_in_mean = np.mean(time)
        print('第{}季度的平均骑行时间是:{:.2f}分钟'.format(index+1,time_in_mean))
        time_mean_list.append(time_in_mean)
    return time_mean_list

def visualize_data(time_mean_list):
    plt.figure()
    plt.bar(range(len(time_mean_list)),time_mean_list)
    plt.show()

def main():
    data_arr_list = collect_data()
    time_in_min_com = process_data(data_arr_list)
    time_mean_list = analyze_data(time_in_min_com)
    visualize_data(time_mean_list)


if __name__ == '__main__':
    main()