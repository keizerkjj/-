import os
import pandas as pd
import matplotlib.pyplot as plt

datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/video_games_sales.csv'


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
    # dropna: 去掉NA值
    cln_data = data_df.dropna()
    # 按年份过滤
    cond = (cln_data['Year'] >=2005) & (cln_data['Year']<=2017)
    filtered_data1 = cln_data[cond]
    cln_fil_data = filtered_data1.copy()
    # 多添加一列，求全球销量
    cln_fil_data['Global_sum'] = cln_fil_data['NA_Sales'] + cln_fil_data['EU_Sales'] \
                 + cln_fil_data['JP_Sales'] + cln_fil_data['Other_Sales']
    print('原始数据有{}行记录，处理后的数据有{}行记录'.format(data_df.shape[0], cln_fil_data.shape[0]))
    return cln_fil_data

def analyze_data(cln_fil_data):
    # 计算top20的游戏，先用sort_values排序，之后得到头20个数据
    top20_games = cln_fil_data.sort_values(by='Global_sum',ascending=False).head(20)

    filter_data = cln_fil_data[cln_fil_data['Global_sum'] >5 ]
    # 注意，以下这一步，首先groupby找出对应的索引列，之后[]里面的是要针对的其他列进行求和处理，因为针对的列有4列，所以需要再加一个[]
    group_df = filter_data.groupby('Publisher')
    data_comp = group_df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum()

    return top20_games,data_comp

def visualize_data(top20_games,data_comp):
    top20_games.to_csv(os.path.join(output_path,'top20_games.csv'),index=False)
    data_comp.to_csv(os.path.join(output_path,'data_comp.csv'))

    top20_games.plot(kind='bar',x='Name',y='Global_sum')
    plt.title('2005-2017 top 20 Games')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'top20_games.png'))
    plt.show()

    data_comp.plot(kind='bar',stacked=True)
    plt.title('Game Sales Comparison (2005 - 2017)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'sales_comp_results.png'))
    plt.show()

def main():
    data_df = collect_data()
    inspect_data(data_df)
    cln_fil_data = process_data(data_df)
    top20_games,data_comp = analyze_data(cln_fil_data)
    visualize_data(top20_games,data_comp)

if __name__ == '__main__':
    main()
