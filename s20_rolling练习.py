import os
import pandas as pd

import matplotlib.pyplot as plt

pm_datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/pm1.csv'
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

pm_df = pd.read_csv(pm_datafile_path)
pm_df['Timestamp'] = pd.to_datetime(pm_df['Timestamp'])
pm_df.set_index('Timestamp', inplace=True)

resampled_df = pm_df.resample('D').last()

resampled_df['pm_3'] = resampled_df['PM'].rolling(window=3).mean()
resampled_df['pm_5'] = resampled_df['PM'].rolling(window=5).mean()
resampled_df['pm_7'] = resampled_df['PM'].rolling(window=7).mean()

resampled_df.to_csv(os.path.join(output_path, 'pm.csv'))
resampled_df[['PM', 'pm_3', 'pm_5', 'pm_7']].plot()
plt.tight_layout()
plt.ylabel('PM value')
plt.savefig(os.path.join(output_path, 'pm.png'))
plt.show()
