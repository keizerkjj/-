import os
import pandas as pd
import matplotlib.pyplot as plt

datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/Beijing_PM.csv'

output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

data_df = pd.read_csv(datafile_path)
cln_data_0 = data_df.dropna()
cln_data = cln_data_0.copy()

cln_data['diff'] = cln_data['PM_China'] - cln_data['PM_US']
cln_data['diff'] = cln_data['diff'].abs()

big10_data = cln_data.sort_values(by='diff',ascending=False).head(10)

# 中国的每年平均pm
year_df = cln_data.groupby('year')[['PM_China','PM_US']].mean()
year_df.plot(kind='bar')
plt.tight_layout()
plt.show()

