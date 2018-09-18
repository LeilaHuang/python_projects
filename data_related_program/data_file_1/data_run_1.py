# 1. 练习：创建一个批量温度转换器
# 题目描述：创建一个批量温度转换器，使其将摄氏温度批量地转换为华氏温度。
# 公式为: f = 1.8 *c + 32，其中 c 为摄氏温度，f为华氏温度。
# 题目要求：使用NumPy中向量化的方法，不能使用循环操作

import os
import numpy as np

data_path = 'data_related_program/data_file_1'
data_filename = 'temp.csv'

data_file = os.path.join(data_path,data_filename)

def get_data():
    temp_data = np.loadtxt(data_file, delimiter=',',dtype='str',skiprows=1)
    return temp_data

def process_data(temp_data):
    # only select the second element in the row
    c_temp_str = temp_data[:, 1]
    c_temp = np.core.defchararray.replace(c_temp_str,' C','')
    f_temp = c_temp.astype('int')*1.8 + 32
    f_temp = f_temp.astype('int').astype('str')
    f_temp_str = np.core.defchararray.join(f_temp,' F')
    f_temp_str = np.core.defchararray.replace(f_temp_str, ' ', '')
    f_temp_str = np.core.defchararray.replace(f_temp_str, 'F', ' F')
    return f_temp_str

def transform_to_file(temp_data,f_temp_str):
    colum_data = temp_data[:,0]
    f_temp_str = [f_temp_str]
    # add 之前的左边一列 data 和我们做好的右边一列data 在一起
    added_data = np.insert(f_temp_str, 0, values = colum_data, axis = 0)
    # .T 是将二维数组转置 （行变列，列变行）
    np.savetxt(data_path+"/output.csv", added_data.T, fmt= '%s', delimiter = ',',comments = '', header = "month,temperature")

def main():
    temp_data = get_data()
    f_temp_str = process_data(temp_data)
    transform_to_file(temp_data,f_temp_str)

if __name__ == '__main__':
    main()

