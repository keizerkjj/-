import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

report_datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/happiness_report.csv'

output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)


def collection_data():
    data_df = pd.read_csv(report_datafile_path)
    return data_df

def process_data(data_df):
    data_df.dropna(inplace=True)
    data_df.sort_values(by=['Year','Happiness Score'],ascending=[True,False],inplace=True)
    return data_df

def analyze_data(data_df):
    #使用apply函数，对特定列进行分组操作
    '''
    def seperate_array(data_array):
        if data_array <= 3:
            score_list = 'Low'
        elif data_array <=5:
            score_list = 'Middle'
        else:
            score_list= 'High'
        return score_list
    data_df['type_Happiness'] =data_df['Happiness Score'].apply(seperate_array)
    '''
    data_df['Level'] = pd.cut(data_df['Happiness Score'], bins=[-np.inf, 3, 5, np.inf]
           , labels=['Low', 'Middle', 'High'])
    # values后面需要带上[xxxx]，这样再下面的pivot_table.columns才能显示出层级
    pivot_table = pd.pivot_table(data_df, index='Region', columns=['Year', 'Level'], values=['Country'], aggfunc='count')

    pivot_table.fillna(0,inplace=True)
    return pivot_table

def visualize_data(pivot_table):

    pivot_table.to_csv(os.path.join(output_path,'happiness.csv'))

    for year in [2015,2016,2017]:
        # 当pivot_table的columns有多列，同时我要访问特定某一列的时候，注意它有层级索引的限制。在这个地方，我要访问year这一列，那么需要考虑country这一上级
        # 如果pivot_table的columns只有一列，那么只需要直接pivot_table.plot就行
        pivot_table['Country',year].plot(kind='bar',stacked=True,title=year)
        plt.tight_layout()
        plt.legend(loc='best')
        plt.savefig(os.path.join(output_path,f'happiness_level{year}.png'))
        plt.show()



def main():
    data_df = collection_data()
    data_df = process_data(data_df)
    data_df = analyze_data(data_df)
    visualize_data(data_df)

if __name__ == '__main__':
    main()

