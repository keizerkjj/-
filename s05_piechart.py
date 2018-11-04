import os
import numpy as np
import matplotlib.pyplot as plt

data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/bikeshare'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_and_process_data():

    year_member_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)
        #通过reshape将单维度的数据转化为 双维度的数据
        member_col = data_arr[:,-1]
        member_type_col = member_col.reshape(-1,1)
        year_member_list.append(member_type_col)

    year_member_type = np.concatenate(year_member_list)
    #print(type(year_member_type))
    return year_member_type

def analyze_data(year_member_type):
    # 过滤出 member 和 casual
    member_num = year_member_type[year_member_type == 'Member'].shape[0]
    casual_num = year_member_type[year_member_type == 'Casual'].shape[0]
    # 拼装成 member_type的list，用于数据展示
    member_type = [member_num,casual_num]
    return member_type

def visualize_data(member_type):
    plt.figure()
    plt.pie(member_type,labels=['Member', 'Casual'], autopct='%.2f%%', shadow=True, explode=(0.05, 0))
    # 使得pie的形状为正圆形
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, './piechart.png'))
    plt.show()

def main():
    year_member_type = collect_and_process_data()
    member_type = analyze_data(year_member_type)
    visualize_data(member_type)
if __name__ == '__main__':
    main()
