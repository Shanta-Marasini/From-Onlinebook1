import shutil,os,send2trash
from pathlib import Path
print('hello Shiva baba my world')

p = Path.home() / 'PycharmProjects'
print(p)
print(type(p))
#copy file
# c = shutil.copy(p/'onlinebook/stringss.py', p/'onlinebook2')
# print(c)
# print(type(c))
# d = shutil.copy(p/'onlinebook\stringss.py',p/'onlinebook2\string2.py')
# print(d)
# print(type(d))

#copy folder
# c = shutil.copytree(p/'onlinebook',p/'onlinebook_copy')
# print(c)
# print(type(c))

#move and not-rename file
# shutil.move('C:\\Users\\User\\PycharmProjects\\onlinebook_copy\\pyper.py',
#             'C:\\Users\\User\\PycharmProjects')

#not-move and not-rename file give same path file name different
# shutil.move('C:\\Users\\User\\PycharmProjects\\onlinebook_copy\\bdays.py',
#             'C:\\Users\\User\\PycharmProjects\\onlinebook_copy\\birthdays.py')

#move and rename file
# shutil.move('C:\\Users\\User\\PycharmProjects\\onlinebook_copy\\listprint.py',
#             'C:\\Users\\User\\PycharmProjects\\pypermove.py')

#delete with os
# os.unlink(p/'pypermove.py')    # has objects arguments
# os.rmdir(folder should be empty)

#delete folder with shutil.rmtree
# shutil.rmtree(p/'onlinebook_copy')    #has object arguments
#This deletions are permanent not irreversible also free up disk space

#send2trash is a third party module that can move files to recycle bins
# send2trash.send2trash('C:\\Users\\User\\PycharmProjects\\todelete.txt')
#Moved to recycle bin