import os
import pandas as pd
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
    # 以下做数值排序，对后续步骤没有实质影响，只是展示实现多系列的排序
    data_df.sort_values(by=['Year','Happiness Score'],ascending=[True,False],inplace=True)
    return data_df

def analyze_data(data_df):
    grouped_happiness_score_series =data_df.groupby(by=['Year','Region'])['Happiness Score'].mean()
    data_df_pivot_table = pd.pivot_table(data_df,index='Region',columns='Year',
                                              values=['Happiness Score','Economy (GDP per Capita)']
                                              ,aggfunc='mean')
    return grouped_happiness_score_series,data_df_pivot_table

def visualize_data(grouped_happiness_score_series,data_df_pivot_table):
    grouped_happiness_score_series.to_csv(os.path.join(output_path,'happiness_series.csv'))
    data_df_pivot_table.to_csv(os.path.join(output_path,'pivot_table.csv'))

    # 利用 pivottable制作的bar chart是多列对比的
    data_df_pivot_table['Happiness Score'].plot(kind='bar',rot=45,title='Happiness score')
    #plt.savefig(os.path.join(output_path,'Happiness_score.png'))
    data_df_pivot_table['Economy (GDP per Capita)'].plot(kind='bar',rot=45, title='GDP')
    #plt.savefig(os.path.join(output_path, 'GDP.png'))

    plt.tight_layout()
    plt.show()




def main():
    data_df = collection_data()
    data_df = process_data(data_df)
    grouped_happiness_score_series,data_df_pivot_table =analyze_data(data_df)
    visualize_data(grouped_happiness_score_series,data_df_pivot_table)



if __name__ == '__main__':
    main()
