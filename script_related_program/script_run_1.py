# 模糊搜索
import os
path = './problem1_files'
files = os.listdir(path)

for f in files:
    if (not f.endswith('.gif')) and ('project30' in f or 'commercial' in f):
        print(f)