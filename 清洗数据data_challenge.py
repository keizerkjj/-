import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dentist_datafile_path = '/Users/likaizhe/Desktop/Data challenge term 1/rawdata_challenge.csv'

output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    data_df = pd.read_csv(dentist_datafile_path)
    return data_df

def processing_data(data_df):
    #print(data_df['age'].unique())
    # 通过使用unique来检查数据是否出现错误值，发现alcohol出现许多极端值
    print(data_df['alcohol'].unique())
    #接下来，考虑利用单词长度来过滤出正确的数据格式
    def fix_alcohol(data):
        if not ((len(data) == 5) or (len(data) == 10)):
            return data[:5]
        else:
            return data
    def fix_right_alcohol(data):
        if data == 'heavy':
            data = 1
        else:
            data = 0
        return data
    def fix_weight(data):
        if data > 1000:
            return data/100
        else:
            return data
    #data_df.drop(columns = ['Unnamed: 0'],inplace=True)
    data_df['right_alcohol'] = data_df['alcohol'].apply(fix_alcohol)
    #print(data_df['right_alcohol'].unique())  这一步是为了确认已经清洁完毕
    # 非常好用！！的映射方法map，这样就不需要重新生成新的一列数据
    data_df['alcohol'] = list(map(fix_right_alcohol,data_df['alcohol']))
    data_df['gum_disease'] = data_df['gum_disease'].fillna(0)
    data_df['tp_fluoride'] = data_df['tp_fluoride'].fillna(0)
    #print(data_df['weight'].unique())
    data_df['weight'] = list(map(fix_weight,data_df['weight']))
    #print(data_df['weight'].unique())
    data_df.to_csv(os.path.join(output_path,'data_clean_1.csv'))



def main():
    data_df = collect_data()
    processing_data(data_df)
if __name__ == '__main__':
    main()



