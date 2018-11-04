import os
import pandas as pd
import matplotlib.pyplot as plt

datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/coffee_menu.csv'


output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    coffee_df = pd.read_csv(datafile_path)
    return  coffee_df

def inspect_data(coffee_df):
    # 查看pandas加载完成数据的 行和列的个数
    print('数据有{}行和{}列'.format(coffee_df.shape[0],coffee_df.shape[1]))
    print('头十个数据的预览')
    print(coffee_df.head(10))
    print('数据信息的预览')
    print(coffee_df.info())
    print('数据信息统计')
    print(coffee_df.describe())

def analyze_data(coffee_df):
    # 选取要的两列数据
    coffee_type = coffee_df['Beverage_category']
    coffee_type = coffee_type.unique()
    print('咖啡的产品类别有：')
    print(coffee_type)
    # 以下是pandas分组数据，运算数据的语句
    coffee_Calories = coffee_df.groupby('Beverage_category')
    type_count = coffee_Calories['Calories'].count()
    calories_mean = coffee_Calories['Calories'].mean()
    return type_count,calories_mean


def visualize_data(type_count,calories_mean):
    type_count.to_csv(os.path.join(output_path, 'category_count.csv'))
    calories_mean.to_csv(os.path.join(output_path, 'calories_mean.csv'))

    type_count.plot(kind = 'bar')
    plt.title('Category Count')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'category_count.png'))

    calories_mean.plot(kind = 'bar')
    plt.title('Calories Count')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'calories_count.png'))

def main():
    coffee_df = collect_data()
    inspect_data(coffee_df)
    type_count, calories_mean = analyze_data(coffee_df)
    visualize_data(type_count,calories_mean)


if __name__ == '__main__':
    main()