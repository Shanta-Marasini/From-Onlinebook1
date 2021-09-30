import os,zipfile
from pathlib import Path
print('hello Shiva baba my world')

#Make a function
def backupToZip(folder):
    os.path.abspath(folder)  #make sure it is a abs path
    number = 1
    while True:
        zipFileName = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFileName):    #if doesnot exists
            break
        number = number + 1                    #if exists

    #Create a new zipfile
    print(f'Creating {zipFileName}....')
    backupZip = zipfile.ZipFile(zipFileName,'w')

    #Walk the entire folder tree and compress the files in each folder
    for folderName, subfolders, fileNames in os.walk(folder):
        #add current folder to zipfile
        backupZip.write(folderName)
        print(f'Adding files in folder:{folderName}')
        #Add all the files in this folder in zip files
        for filename in fileNames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't back up the backup ZIP files
            backupZip.write(os.path.join(folderName, filename))

    backupZip.close()



# backupToZip('C:\\Users\\User\\PycharmProjects\\pyShop')
allMethods = dir(ZeroDivisionError)
for x in allMethods:
    print(x)


