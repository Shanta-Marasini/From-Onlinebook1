from pathlib import Path
import os
print('Hello Shiva baba my world')

path = Path('c','Users','User')
print(path)

files = ['hello','hi','go']
for fil in files:
    print(Path(r'C:\Users\User',fil))

#Current worling directory  cwd
print(Path.cwd())

# #Change working directory
# os.chdir('C:\\Users\\User\\PycharmProjects\\onlinebook')
# print(Path.cwd())
#Home directory for user
print(Path.home())
#making new directories
# os.makedirs('C:\\Users\\User\\aanew\\hello')  #oneway
# Path(r'C:\Users\User\aanew\pathdir').mkdir()

#is an absolute path or not
check = Path.cwd()
print(check.is_absolute())
nextcheck = Path(r'onlinebook/stringss.py').is_absolute()
print(nextcheck)
#change relative path to absolute
abspath = Path.cwd()/Path('.\ques10.py')
print(abspath)

#using os.path
a = os.path.abspath('.')
print(a)
b = os.path.isabs('.\\ques10.py')
print(b)
c = os.path.relpath('C:\\Users')
print(c)
print()
#getting parts of file path
p = Path.cwd()/'path.py'
print(p)
print(p.anchor)
print(p.drive)
print(p.parent)
print(p.name)
print(p.stem)
print(p.suffix)
#parents attribute
print(p.parents[0])
print(p.parents[1])
print(p.parents[2])
print(p.parents[3])
print(p.parents[4])
print(len(p.parents))
#alternative
for i in p.parents:
    print(i)
#alternative
for i in range(len(p.parents)):
    print(p.parents[i])
splitt = os.path.split(p)
print(splitt[0].split('\\'))


