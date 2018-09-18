# 删除重复的文件。包括不同文件夹内的重复文件
import os
import filecmp

pathPic1 = './problem3_files/pic1'
pathPic2 = './problem3_files/pic2'
listFilePic1 = os.listdir(pathPic1)
listFilePic2 = os.listdir(pathPic2)

# find same file in one path
def cmpFile(dir,path):
    dupList = []
    for i in range(len(dir)):
        for j in range(i+1,len(dir)):
            if filecmp.cmp(path+'/'+dir[i],path+'/'+dir[j]) == True:
                dupList.append(dir[i])
    return list(set(dupList))


# find same file in 2 files
def cmpFiles(dir1,dir2,path1,path2):
    dupList = []
    for i in range(len(dir1)):
        for j in range(len(dir2)):
            if filecmp.cmp(path1+'/'+dir1[i],path2+'/'+dir2[j]) == True:
                dupList.append(path1+'/'+dir1[i])
    return list(set(dupList))

# delete same object in one file
def deletSameObjInFile(listFilePic,pathPic):
    dupTuple = cmpFile(listFilePic, pathPic)
    for i in range(len(dupTuple)):
        os.remove(pathPic + '/' + dupTuple[i])

def main():
    pass
    # delete same object in one file
    deletSameObjInFile(listFilePic1,pathPic1)
    deletSameObjInFile(listFilePic2, pathPic2)
    # delete files in two duplicatedList
    dupList = cmpFiles(listFilePic1,listFilePic2,pathPic1,pathPic2)
    for l in dupList:
        os.remove(l)

if __name__ == '__main__':
    main()



