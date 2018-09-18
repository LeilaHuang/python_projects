# 使用Pandas的版本
# 练习：使用柱状图可视化 PM2.5数值
# # 题目要求:
# # * 使用Pandas查看数据文件的基本信息
# # * 使用Pandas进行数据分析及可视化

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_path = './'
data_filename = 'Beijing_PM.csv'

def collect_data():
    data_file = os.path.join(data_path, data_filename)
    data_df = pd.read_csv(data_file)
    return data_df

def analyze_data(data_df):
    year_col = data_df['year']
    years = year_col.unique()

    years_grouped = data_df.groupby('year')
    years_mean_PM = years_grouped['PM_US'].mean()
    return  years_mean_PM

def save_and_visualize_data(years_mean_PM):
    years_mean_PM.to_csv('./years_mean_PM.csv')

    years_mean_PM.plot(kind='bar')
    plt.title('years_count')
    plt.tight_layout()
    plt.savefig('BeijingPM_2.png')
    plt.show()

def main():
    data_df = collect_data()
    years_mean_PM =analyze_data(data_df)
    save_and_visualize_data(years_mean_PM)

if __name__ == '__main__':
    main()