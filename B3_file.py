import os,zipfile
print('Hello my world')

#back up a fresh folder to zipfile

def backUpToZip(folder):
    folder = os.path.abspath(folder)
    zipFileName = os.path.basename(folder) + '.zip'
    zipFilePath = os.path.join('F:\\backUp',zipFileName)
    print(zipFilePath)
    zipFileObj = zipfile.ZipFile(zipFilePath,'w')

    for folderName, subfolders, filenames in os.walk(folder):
        zipFileObj.write(folderName)


        for filename in filenames:
            zipFileObj.write(os.path.join(folderName, filename))

    zipFileObj.close()

backUpToZip('C:\\Users\\User\\PycharmProjects\\onlinebook')