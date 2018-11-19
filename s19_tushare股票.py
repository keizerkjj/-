import os
import pandas as pd
import matplotlib.pyplot as plt
import tushare

stock_code = '600519'

output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    stock_df = tushare.get_k_data(code=stock_code,start='2010-01-01',end='2018-11-1',ktype='60')
    return stock_df

def process_data(stock_df):
    # 将dataframe中的日期转化成日期格式
    stock_df['date'] = pd.to_datetime(stock_df['date'])
    # 将日期转化成index类型，使得能够完成resample
    stock_df.set_index('date',inplace=True)
    # 得到有index的df之后，进行resample，最后取最后值(最后一个小时的开始值和结束值），所以最后的start_time其实是最后一个小时开始的值
    resampled_df =stock_df.resample('D').last()
    resampled_df.dropna(inplace=True)
    return resampled_df

def analyze_data(resampled_df):
    #得到日均线后，计算5日均线，30日均线，60日均线
    resampled_df['stock_5'] = resampled_df['close'].rolling(window=5).mean()
    resampled_df['stock_30'] = resampled_df['close'].rolling(window=30).mean()
    resampled_df['stock_60'] = resampled_df['close'].rolling(window=60).mean()
    return resampled_df

def visualize_data(resampled_df):
    resampled_df.to_csv(os.path.join(output_path,'stock_trend.csv'))
    resampled_df[['close','stock_5','stock_30','stock_60']].plot()
    plt.ylabel('Price')
    plt.show()



def main():
    stock_df = collect_data()
    resampled_df = process_data(stock_df)
    resampled_df = analyze_data(resampled_df)
    visualize_data(resampled_df)

if __name__ == '__main__':
    main()