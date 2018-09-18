# 题目描述：按月份统计每月气温的最大值、最小值及平均值
# 题目要求:使用NumPy中布尔型数组进行数据过滤
# 数据文件：
# 数据源下载地址：https://video.mugglecode.com/temp2.csv。temp2.csv
# 中包含了2018年1-3月北京的气温（每日的最低温度）。每行记录为1天的数据。
# 共2列数据，第1列month为月份，第2列temperature为摄氏温度

import os
import numpy as np
import matplotlib.pyplot as plt

data_path = './'
data_filename = 'temp2.csv'
month_temp_list = []

def get_data():
    data_file = os.path.join(data_path, data_filename)
    temp_data = np.loadtxt(data_file, delimiter=',',dtype='str',skiprows=1)
    return temp_data

def process_temp_data_by_month(temp_data,month):
    bool_arr = temp_data[:, 0] == month
    filtered_temp = temp_data[bool_arr]
    mean_temp = np.mean(filtered_temp[:,1].astype('float'))
    min_temp = np.min(filtered_temp[:,1].astype('float'))
    max_temp = np.max(filtered_temp[:, 1].astype('float'))
    month_temp = [month, min_temp, mean_temp, max_temp]
    month_temp_list.append(month_temp)
    return month_temp_list

def save_and_output_data(month_temp_list):
    # for output
    min_temp_list = []
    mean_temp_list = []
    max_temp_list = []
    for idx in range(len(month_temp_list)):
        min_temp = month_temp_list[idx][1]
        mean_temp = month_temp_list[idx][2]
        max_temp = month_temp_list[idx][3]
        print('{}月的最低温度是{}摄氏度，平均温度是{:+.2f}摄氏度, 最大温度是{}摄氏度'.format(idx+1,min_temp,mean_temp,max_temp))
        min_temp_list.append(min_temp)
        mean_temp_list.append(mean_temp)
        max_temp_list.append(max_temp)

    # save to output.csv
    anaylzed_temp = np.array(month_temp_list)
    np.savetxt('output.csv',anaylzed_temp,delimiter = ',', fmt ='%s',comments = '', header = 'month,min temperature,mean temperature,max temperature')
    # for visualize
    plt.figure()
    n = len(month_temp_list)
    index = np.arange(n)
    bar_width = 0.3
    # min_temp_list,mean_temp_list,max_temp_list 必须是list 不然就是一个值
    plt.bar(index, min_temp_list, bar_width,align='center',color='b',
                 label='Jan')
    plt.bar(index+bar_width, mean_temp_list, bar_width, align='center', color='g',
            label='Feb')
    plt.bar(index + 2*bar_width, max_temp_list, bar_width, align='center', color='y',
            label='Mar')
    plt.xlabel('Month')
    plt.ylabel('temperature')
    plt.title('Month temperatures')
    plt.xticks(index + bar_width, ('min', 'mean', 'max'))
    plt.legend(loc = 'best')
    plt.tight_layout()
    plt.savefig('month_temperature.png')
    plt.show()

def main():
    temp_data = get_data()
    process_temp_data_by_month(temp_data, '1')
    process_temp_data_by_month(temp_data, '2')
    process_temp_data_by_month(temp_data, '3')
    save_and_output_data(month_temp_list)

if __name__ == '__main__':
    main()