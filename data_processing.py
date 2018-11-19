import os
import pandas as pd

dentist_datafile_path = '/Users/likaizhe/Desktop/raw_data.csv'

output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)
def collect_data():
    data_df = pd.read_csv(dentist_datafile_path)
    return data_df
def process_data(data_df):
    def transform_data(data_array):
        if data_array == 'heavy':
            data_array = 1
        else:
            data_array = 0
        return data_array

    data_df['processed_alcohol'] = data_df['alcohol'].apply(transform_data)
    data_df['adjusted_gum_disease']=data_df['gum_disease'].fillna(0)
    return data_df

def analyze_data(data_df):
    data_df.to_csv(os.path.join(output_path,'datatry_11.17.csv'))


def main():
    data_df = collect_data()
    data_df= process_data(data_df)
    analyze_data(data_df)

if __name__ == '__main__':
    main()