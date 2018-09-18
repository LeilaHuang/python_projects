# 监测 image 文件夹，如果包含的文件大于等于 5 个，
# 则将这些文件压缩到 archive1.zip 文件中，并删除这些文件。
# 当再次监测到文件多于 5 个的时候，生成 archive2.zip 压缩包，以此类推
import os
import shutil

path = './problem3_image'
count = 1

def zip_it(path,dest_folder):
    shutil.make_archive('./'+dest_folder,'zip',path)

def delete(files):
    for f in files:
        os.remove(path+'/'+f)

while True:
    files = os.listdir(path)
    dest_folder = 'archive'
    # if len(files) == 0:
    #     break
    if len(files) >= 5:
        zip_it(path, dest_folder + str(count))
        count = count + 1
        delete(files)

