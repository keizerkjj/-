import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/pokemon.csv'


output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    #读取特定的列
    read_col = ['Name', 'Type_1', 'Total', 'HP', 'Attack', 'Defense', 'Speed', 'Height_m', 'Weight_kg', 'Catch_Rate']
    data_df = pd.read_csv(datafile_path,usecols= read_col)
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

def analyze_data_bytype(cln_data,attr):
    sns.boxplot(x='Type_1',y=attr,data=cln_data)
    plt.savefig(os.path.join(output_path, 'boxplot.png'))
    plt.show()


def analyze_dual(cln_data,var1,var2):
    sns.jointplot(x=var1, y=var2, data=cln_data)
    plt.show()

def analyze_corr(cln_data):
    #设置画布的大小，使得x和y轴不会出现字体重合
    plt.figure(figsize=(10, 8))
    corr_data = cln_data.corr()
    sns.heatmap(corr_data,annot=True,square=True)
    plt.show()

def main():
    data_df = collect_data()
    inspect_data(data_df)
    cln_data = process_data(data_df)
    analyze_data_bytype(cln_data,attr='Attack')
    analyze_dual(cln_data,var1='HP',var2='Attack')
    analyze_corr(cln_data)
    #visualize_data(top20_games,data_comp)

if __name__ == '__main__':
    main()