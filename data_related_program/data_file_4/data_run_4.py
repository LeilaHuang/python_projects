# 题目描述：统计1-3月气温在-10℃~10℃的天数统计直方图

import os
import numpy as np
import matplotlib.pyplot as plt

data_path = './'
data_filename = 'temp2.csv'
month_temp_list = []

def get_data():
    data_file = os.path.join(data_path, data_filename)
    temp_data = np.loadtxt(data_file, delimiter=',',dtype='int',skiprows=1)
    return temp_data

def analyze_data(temp_data, month):
    # np.logical_and() one time can only use two values
    bool_arr = np.logical_and(temp_data[:, 0] == month, np.logical_and(temp_data[:, 1] <= 10, temp_data[:, 1] >= -10 ))
    filtered_month_temp_data = temp_data[bool_arr][:,1]
    return filtered_month_temp_data

def output_histogram(filtered_month_temp_data_1, filtered_month_temp_data_2, filtered_month_temp_data_3):
    fig = plt.figure(figsize=(9, 8))
    # count from 1 , the third number is the order
    ax1 = fig.add_subplot(1, 3, 1)
    ax2 = fig.add_subplot(1, 3, 2, sharey = ax1)
    ax3 = fig.add_subplot(1, 3, 3, sharey = ax1)

    hist_range = (-10, 10)
    # 多少份
    n_bins = 10
    #month 1
    ax1.hist(filtered_month_temp_data_1, range = hist_range, bins = n_bins)
    ax1.set_xticks(range(-10, 11, 5))
    ax1.set_title('month1')
    ax1.set_ylabel('Count')
    ax1.set_xlabel('temperature')
    #month2
    ax2.hist(filtered_month_temp_data_2, range = hist_range, bins = n_bins)
    ax2.set_xticks(range(-10, 11, 5))
    ax2.set_title('month2')
    ax2.set_ylabel('Count')
    ax2.set_xlabel('temperature')
    #month3
    ax3.hist(filtered_month_temp_data_3, range = hist_range, bins = n_bins)
    ax3.set_xticks(range(-10, 11, 5))
    ax3.set_title('month3')
    ax3.set_ylabel('Count')
    ax3.set_xlabel('temperature')

    # plt.tight_layout()
    plt.savefig('output.png')
    plt.show()

def main():
    temp_data = get_data()
    filtered_month_temp_data_1 = analyze_data(temp_data, 1)
    filtered_month_temp_data_2 = analyze_data(temp_data, 2)
    filtered_month_temp_data_3 = analyze_data(temp_data, 3)
    output_histogram(filtered_month_temp_data_1,filtered_month_temp_data_2,filtered_month_temp_data_3)

if __name__ == '__main__' :
    main()
