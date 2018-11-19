import os
import pandas as pd
import matplotlib.pyplot as plt

user_device_datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/mobile_data/user_device.csv'

user_usage_datafile_path = '/Users/likaizhe/Desktop/Python/Data_Analytics/data_pd 2/mobile_data/user_usage.csv'

output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def collect_data():
    device_df = pd.read_csv(user_device_datafile_path)
    usage_df = pd.read_csv(user_usage_datafile_path)
    return device_df,usage_df

def process_data(device_df,usage_df):
    transfer_df = device_df['platform_version'].astype('str')
    device_df['system'] = device_df['platform'].str.cat(transfer_df,sep='_')
    merged_df = pd.merge(device_df,usage_df,how='inner',on='user_id')
    return merged_df

def analyze_data(merged_df):
    mean_series = merged_df.groupby('system')['monthly_mb'].mean()
    mean_series.sort_values(ascending=False,inplace=True)
    return mean_series

def visualize_data(mean_series):
    mean_series.to_csv(os.path.join(output_path,'mean_series.csv'))
    plt.figure(figsize=(10, 8))
    mean_series.plot(kind='bar',rot=45)
    plt.ylabel('Monthly data usage')
    plt.savefig(os.path.join(output_path,'mean_series.png'))
    plt.tight_layout()
    plt.show()

def main():
    device_df,usage_df = collect_data()
    merged_df = process_data(device_df,usage_df)
    means_series = analyze_data(merged_df)
    visualize_data(means_series)


if __name__ == '__main__':
    main()
