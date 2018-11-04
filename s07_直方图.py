import os
import numpy as np
import matplotlib.pyplot as plt

data_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/bikeshare'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)
hist_range = (0,180)
hist_bins = 12
def collect_and_process_data():
    year_weather_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        # 注意在读取data_file的时候，生成的样式一般选择为str，否则像"2017-04-01"这种数据将无法读取
        data_arr = np.loadtxt(data_file, delimiter=',',dtype='str',skiprows=1)
        duration_col = data_arr[:,0].reshape(-1, 1)
        member_col = data_arr[:,-1].reshape(-1, 1)
        du_mem_cols = np.concatenate([duration_col,member_col],axis=1)
        year_weather_list.append(du_mem_cols)
    year_arr = np.concatenate(year_weather_list,axis=0)
    member_arr = year_arr[year_arr[:,1] == 'Member']
    casual_arr = year_arr[year_arr[:,1] == 'Casual']
    # 因为前面读取的方式是str，所以需要转换成float再进行运算
    member_min = member_arr[:,0].astype('float')/ 1000 / 60
    casual_min = casual_arr[:,0].astype('float')/ 1000 / 60
    return member_min,casual_min

def analyze_data(member_min,casual_min):
    mem_hist,mem_bins = np.histogram(member_min, range=hist_range, bins= hist_bins)
    cas_hist,cas_bins = np.histogram(casual_min, range=hist_range, bins=hist_bins)
    print(f'会员直方图的信息是:{mem_hist},边界是：{mem_bins}')
    print(f'非会员直方图的信息是:{cas_hist},边界是：{cas_bins}')

def visualize_data(member_min,casual_min):
    fig = plt.figure(figsize=(10,5))
    # 将两个直方图放置于一个画布中
    ax1 = fig.add_subplot(1,2,1)
    # sharey使得两个图的纵坐标是一样的
    ax2 = fig.add_subplot(1,2,2,sharey = ax1)

    ax1.hist(member_min, range=hist_range, bins= hist_bins)
    ax1.set_xticks(range(0, 181, 15))
    ax1.set_title('Member')
    ax1.set_ylabel('Count')

    ax2.hist(casual_min,range=hist_range, bins= hist_bins)
    ax2.set_xticks(range(0, 181, 15))
    ax2.set_title('Casual')
    ax2.set_ylabel('Count')

    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'type_histogram.png'))
    plt.show()

def main():
    member_min,casual_min = collect_and_process_data()
    analyze_data(member_min,casual_min)
    visualize_data(member_min,casual_min)


if __name__ == '__main__':
    main()