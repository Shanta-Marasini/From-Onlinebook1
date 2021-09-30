import os,zipfile
from pathlib import Path
print('hello Shiva baba my world')

#Read a zipfile
#ZipFile object
# exampleZip = zipfile.ZipFile('F:\\backUp\\onlinebook.zip')
# print(exampleZip.namelist())
#single file info ZipInfo
# spamInfo = exampleZip.getinfo('example/spam.txt')
# print(spamInfo)
# print(spamInfo.file_size)
# print(spamInfo.compress_size)

#extract zipfile
#in cwd onlinebook2
# exampleZip.extractall()

#in pycharmprojects directory
# exampleZip = zipfile.ZipFile('C:\\Users\\User\\Downloads\\DB.Browser.for.SQLite-3.11.2-win64')
# print(Path.exists('C:\\Users\\User\\Downloads\\DB.Browser.for.SQLite-3.11.2-win64'))
# exampleZip.extractall('C:\\Users\\User')

# exampleZip.extractall('C:\\Users\\User\\PycharmProjects')

#single file
# exampleZip.extract('example/spam.txt')
# exampleZip.extract('example/spam.txt','C:\\Users\\User\\PycharmProjects')
