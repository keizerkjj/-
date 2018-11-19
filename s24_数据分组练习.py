import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pm_datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/pm2.csv'
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

data_df = pd.read_csv(pm_datafile_path)
data_df.dropna()
data_df['Level'] = pd.cut(data_df['PM'],bins=[-np.inf,50,100,500],labels=['Excellent','Good','Bad'])
pivot_table = pd.pivot_table(data_df,index='Year',columns=['Level'],values=['Day'],aggfunc='count')
pivot_table.to_csv(os.path.join(output_path,'pm_level.csv'))
pivot_table.plot(kind='bar',stacked=True,title='PM_level')
plt.legend(loc = 'best')
plt.tight_layout()
plt.savefig(os.path.join(output_path, 'pm_level.png'))
plt.show()