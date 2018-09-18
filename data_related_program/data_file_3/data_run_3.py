# * 题目描述：将1-3个月份的气温数据进行合并，并使用饼状图可视化所有数据的零上气温和零下气温的天数占比情况。


import os
import numpy as np
import matplotlib.pyplot as plt

data_path = './data_temp'
data_filenames = ['201801_temp.csv','201802_temp.csv','201803_temp.csv']

def get_data():
    temp_data_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        temp_data = np.loadtxt(data_file, delimiter = ',', dtype = 'int', skiprows = 1 )
        temp_data_list.append(temp_data)
    months_temp_data = np.concatenate(temp_data_list)
    months_temp_data.reshape(-1,1)
    return months_temp_data

def analyze_data(months_temp_data):
    bool_arr_pos = months_temp_data[:] > 0
    bool_arr_neg = months_temp_data[:] < 0
    # get counts of pos and neg temp data -> to create pie chart only need the %  PS:no need for the data
    filtered_temp_pos = months_temp_data[bool_arr_pos].shape[0]
    filtered_temp_neg = months_temp_data[bool_arr_neg].shape[0]
    all_temp = [filtered_temp_pos, filtered_temp_neg]
    return all_temp

def create_pie_chart(all_temp):
    plt.figure()
    plt.pie(all_temp,labels=['>0','<0'],autopct='%.2f%%',shadow=False,explode=(0.05,0))
    plt.axis('equal')
    plt.tight_layout()
    # plt.title('temperature positive and negative')
    plt.savefig('output.png')
    plt.show()

def main():
    months_temp_data = get_data()
    all_temp = analyze_data(months_temp_data)
    create_pie_chart(all_temp)

if __name__ == '__main__':
    main()
