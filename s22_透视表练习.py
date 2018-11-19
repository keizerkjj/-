import os
import pandas as pd
import matplotlib.pyplot as plt

pm_datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/pm2.csv'
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

data_df = pd.read_csv(pm_datafile_path)

grouped_table = data_df.groupby(by=['Year','Month'])['PM'].mean()

pivot_table = pd.pivot_table(data_df,index='Month',columns='Year',values='PM',aggfunc='mean')

pivot_table.plot(kind='bar',title='PM Value',rot=45)
plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig(os.path.join(output_path, 'month_pm.png'))
plt.show()
