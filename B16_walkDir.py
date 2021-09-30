import os
print('Hello Shiva baba my world')

# p = 'C:\\Users\\User\\PycharmProjects\\delicious'
# for cFolderName,subfolders,filenames in os.walk(p):
#     print('The current folder is:'+ cFolderName)
#
#     for subfolder in subfolders:
#         print('SUBFOLDER of ' + cFolderName + "is:" + subfolder)
#
#     for filename in filenames:
#         print('FILENAME of ' + cFolderName + 'is:' + filename)
#
#     print('')

pp = 'C:\\Users\\User\\PycharmProjects\\onlinebook'
for folderName, subfolders, filenames in os.walk(pp):
    print('Current folder:' + folderName)

    for subfolder in subfolders:
        print('Subfolder of ' + folderName +'is : ' + subfolder)

    for filename in filenames:
        print('Filename of ' + folderName + 'is : ' + filename)

    print('')