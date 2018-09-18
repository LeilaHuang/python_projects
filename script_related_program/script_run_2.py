# 1. 把 jpg,png,gif 文件夹中的所有文件移动到 image 文件夹中，然后删除 jpg,png,gif 文件夹
# 2. 把 doc,docx,md,ppt 文件夹中的所有文件移动到 document 文件夹中，然后删除
import os
import shutil

path = './problem2_files'
files = os.listdir(path)

# check the image and document is exist or not
def checkFile(wantFolder):
    folder_name = './problem2_files/' + wantFolder
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def movefile(FT,DT):
    file_type = './problem2_files/'+ FT
    dest = './problem2_files/' + DT
    for f in os.listdir(file_type):
        shutil.move(file_type+'/'+f,dest)

def forFile(type,place,dest_file):
    if (type in place):
        checkFile(dest_file)
        movefile(type, dest_file)

for f in files:
    forFile('png',f,'image')
    forFile('jpg', f, 'image')
    forFile('gif', f, 'image')
    forFile('doc', f, 'document')
    forFile('docx', f, 'document')
    forFile('md', f, 'document')
    forFile('ppt', f, 'document')

for f in files:
    if len(os.listdir(path+'/'+f)) == 0:
        os.removedirs(path+'/'+f)



