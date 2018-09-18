# 用了numpy
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
    temp_data = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)

    year_col = temp_data[:, 0].reshape(-1, 1)
    pmUS_col = temp_data[:, -1].reshape(-1, 1)
    pmUS_year = np.concatenate([year_col, pmUS_col], axis = 1)
    # because the pm has NA data, we need to filter it
    pmUS_year = pmUS_year[pmUS_year[:,1] != 'NA'].astype('int')

    year_PM_list = []
    one_PM = pmUS_year[pmUS_year[:, 0] == 2013]
    two_PM = pmUS_year[pmUS_year[:, 0] == 2014]
    three_PM = pmUS_year[pmUS_year[:, 0] == 2015]
    # np.mean(a, axis=0) 横向取平均值  axis =1 纵向取平均值
    one_mean_PM = np.mean(one_PM, axis = 0)
    two_mean_PM = np.mean(two_PM, axis = 0)
    three_mean_PM = np.mean(three_PM, axis = 0)
    year_PM_list.append(one_mean_PM)
    year_PM_list.append(two_mean_PM)
    year_PM_list.append(three_mean_PM)
    # np array to dataFrame
    year_PM_list_df = pd.DataFrame(year_PM_list)
    return year_PM_list_df

def visualized_data(year_PM_list_df):
    bar_locs = np.arange(3)
    bar_width = 0.35

    plt.figure()
    plt.bar(bar_locs, year_PM_list_df[1][:],bar_width,alpha = 0.7)
    plt.xticks(bar_locs, (2013,2014,2015) )
    plt.title('Beijing PM2.5 in 2013-2015')
    plt.ylabel('PM2.5')
    plt.legend(loc='best')

    plt.tight_layout()
    plt.savefig('Beijing_PM.png')
    plt.show()

    pass

def main():
    year_PM_list_df = collect_data()
    visualized_data(year_PM_list_df)

if __name__ == '__main__':
    main()
