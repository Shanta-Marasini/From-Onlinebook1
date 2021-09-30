import os
from pathlib import Path
print('Hello Shiva baba my world')
# pathh = Path.cwd()/'path.py'
# print(pathh)
# size = os.path.getsize(pathh)
# print(f'{size} bytes')
# files = os.listdir(Path.cwd())
# print(f'no of files:{files}')
#
# #Total file size of dictionary
# totalSize = 0
# for filename in os.listdir(Path.cwd()):
#     totalSize += os.path.getsize(os.path.join(Path.cwd(),filename))
#
# print(f'{totalSize} bytes')

#glob method
# count = 0
# p = Path.cwd()
# print(p.glob('*'))
# print(list(p.glob('*')))
# spfile = list(p.glob('*.py'))
# print(list(p.glob('path?.py')))
# for files in spfile:
#     print(files)
#     count += 1

#Checking path validity
p = Path('C:\\Windows')
print(p.exists())
print(p.is_file())
print(p.is_dir())
print()
print(os.path.exists(p))
print(os.path.isfile(p))
print(os.path.isdir(p))

