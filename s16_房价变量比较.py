import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/house_data.csv'


output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    data_df = pd.read_csv(datafile_path)
    return data_df

def inspect_data(data_df):
    print('数据有{}行和{}列'.format(data_df.shape[0], data_df.shape[1]))
    print('头十个数据的预览')
    print(data_df.head(10))
    print('数据信息的预览')
    print(data_df.info())
    print('数据信息统计')
    print(data_df.describe())

def process_data(data_df):
    cln_data = data_df.dropna()
    print('原始数据有{}行记录，处理后的数据有{}行记录'.format(data_df.shape[0], cln_data.shape[0]))
    return cln_data

def analyze_price_bytype(cln_data,attr):
    sns.boxplot(x=attr,y='price',data=cln_data)
    plt.show()


def analyze_dual(cln_data,var1,var2):
    sns.jointplot(x=var1, y=var2, data=cln_data)
    plt.show()

def analyze_corr(cln_data):
    plt.figure(figsize=(10, 8))
    corr_data = cln_data.corr()
    sns.heatmap(corr_data,annot=True)
    plt.show()

def main():
    data_df = collect_data()
    inspect_data(data_df)
    cln_data = process_data(data_df)
    analyze_price_bytype(cln_data,attr='bedrooms')
    analyze_dual(cln_data,var1='bathrooms',var2='price')
    analyze_corr(cln_data)

if __name__ == '__main__':
    main()