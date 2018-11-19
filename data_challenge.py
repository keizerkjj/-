import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dentist_datafile_path = '/Users/likaizhe/Desktop/Data challenge term 1/perio_study.csv'

output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

data_df = pd.read_csv(dentist_datafile_path)
print(data_df.head(10))
print(data_df.info())

#filter_df =data_df.
filter_df =data_df.fillna(int(data_df['gum_disease'].mean()))
data_df_1 = filter_df.fillna(int(data_df['tp_fluoride'].mean()))


data_df_1.to_csv(os.path.join(output_path,'fill_na.csv'))
print('*'*100)
#print(data_df.head(10))
#print(data_df.info())
