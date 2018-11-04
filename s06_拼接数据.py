import os
import numpy as np
import matplotlib.pyplot as plt

data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_temp'
data_filenames = ['201801_temp.csv','201802_temp.csv','201803_temp.csv']
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_and_process_data():

    month_weather_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file, delimiter=',', skiprows=1)
        #month_col = data_arr[:,0].reshape(-1,1)
        # 通过观察数据文件，csv中的数据结构已经是可以直接作为分析的二维度结构，所以不需要进行reshape
        month_weather_list.append(data_arr)

    total_month = np.concatenate(month_weather_list)
    #print(type(year_member_type))
    return total_month

def analyze_data(total_month):
    # 过滤出 member 和 casual
    zero_up = total_month[total_month >= 0].shape[0]
    zero_down = total_month[total_month < 0].shape[0]
    # 拼装成 member_type的list，用于数据展示
    weather_temp = [zero_up,zero_down]
    return weather_temp

def visualize_data(member_type):
    plt.figure()
    plt.pie(member_type,labels=['Member', 'Casual'], autopct='%.2f%%', shadow=True, explode=(0.05, 0))
    # 使得pie的形状为正圆形
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, './weather_chart.png'))
    plt.show()

def main():
    total_month = collect_and_process_data()
    weather_temp = analyze_data(total_month)
    visualize_data(weather_temp)





if __name__ == '__main__':
    main()