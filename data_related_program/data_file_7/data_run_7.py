# * 题目描述：
# 1. 添加一列diff用于比较中国环保部和美国使馆检测的PM2.5值的差异（两列数据的绝对值差）
# 2. 找出差别最大的10天的记录
# 3. 使用分组柱状图比较中国环保部和美国使馆检测的每年平均PM2.5的值

import os
import pandas as pd
import matplotlib.pyplot as plt

data_path = './'
data_filename = 'Beijing_PM.csv'
output_path = './output'
if not os.path.exists(output_path):
    os.makedirs(output_path)

def get_data():
    data_file = os.path.join(data_path, data_filename)
    data_df = pd.read_csv(data_file)
    return data_df

def analyze_data(data_df):
    # drop data = 0
    data_df = data_df[(data_df[['PM_US','PM_China']] != 0).all(1)]
    clean_data_df = data_df.dropna()
    filtered_data_df = clean_data_df.copy()
    filtered_data_df['compared PM'] = abs(clean_data_df['PM_China'] - clean_data_df['PM_US'])

    top10_data = filtered_data_df.sort_values(by = 'compared PM', ascending=False).head(10)
    filtered_data_year_df = filtered_data_df.groupby('year').mean()
    # only add china and us data, drop month and day
    filtered_data_year_df = filtered_data_year_df[['PM_China','PM_US']]
    return top10_data,filtered_data_year_df

def visualize_data(top10_data,filtered_data_year_df):
    top10_data.to_csv(os.path.join(output_path, 'top10_compared_PM_data.csv'))
    filtered_data_year_df.to_csv(os.path.join(output_path, 'filtered_data_df.csv'))

    top10_data[['year','compared PM']].plot(kind='bar', x = 'year')
    plt.title('Top 10 compared PM in China and US')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'top10_compared_PM_data.png'))
    plt.show()

    filtered_data_year_df.plot.bar(stacked = True)
    plt.title('mean PM2.5 of China and US ')
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'top10_compared_PM_data.png'))
    plt.show()

def main():
    data_df = get_data()
    top10_data, filtered_data_year_df = analyze_data(data_df)
    visualize_data(top10_data,filtered_data_year_df)

if __name__ == '__main__':
    main()

