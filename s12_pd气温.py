import os
import pandas as pd
import matplotlib.pyplot as plt

datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/Beijing_PM.csv'


output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)


data_df = pd.read_csv(datafile_path)
print('数据有{}行和{}列'.format(data_df.shape[0], data_df.shape[1]))
print('头十个数据的预览')
print(data_df.head(10))
print('数据信息的预览')
print(data_df.info())
print('数据信息统计')
print(data_df.describe())

month_group = data_df.groupby('month')
mean_pm = month_group['PM_China'].mean()

mean_pm.plot(kind='bar')
plt.title('PM_mean')
plt.tight_layout()
plt.savefig(os.path.join(output_path, 'mean_PM.png'))