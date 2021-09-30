import re,os,shutil
print("Hello my world")

#renaming files
#shutil.move(s,s)   regexes os.listdir or os.walk

#1.create a regex to match files of any type
fileObj = re.compile(r'.*\.py')

fileNo = 1
files = os.listdir('C:\\Users\\User\\PycharmProjects\\onlinebook2')
for x in files:
    matchFile = fileObj.search(x)
    if matchFile == None:
        print(x)
        print('no match')
        continue
    renameFile = f'B{fileNo}_' + matchFile.group()
    print(renameFile)
    #get the full aboulute file paths
    oldname = os.path.join('C:\\Users\\User\\PycharmProjects\\onlinebook2',x)
    newname = os.path.join('C:\\Users\\User\\PycharmProjects\\onlinebook2',renameFile)
    shutil.move(oldname,newname)
    print(oldname)
    print('to')
    print(newname)
    fileNo +=1

#remove trailing 0's
#fileObj = re.compile(r'(\D+)(0+)(.*)(\.(.*){1,3})')
#renameFile = mo.group(1)+mo.group(3)+mo.group(4)



