import shelve,pprint,mycats
print('hello Shiva baba my world')

#1 through shleve method
#save files to a file as directory style
# shelveFile = shelve.open('mydata')
# cats = ['hi','hello','Bye']
# shelveFile['cats'] = cats
# shelveFile.close()

# shelfFile = shelve.open('mydata')
# print(type(shelfFile))
# print(shelfFile['cats'])
# shelfFile.close()

#methods return list like values
# shelfFile = shelve.open('mydata')
# print(list(shelfFile.keys()))
# print(list(shelfFile.values()))

#2 through pprint.ppformat method
# cats = [ {'name' : 'hany', 'height': '5 cm'},
#          {'name' : 'hanu', 'height': '6 cm'}]           #list{directory}
#
# fileObj = open('mycats.py','w')
# fileObj.write('cats=' +pprint.pformat(cats)+ '\n')
# fileObj.close()

#retrive data
print(mycats.cats)
print(mycats.cats[0])
print(mycats.cats[0]['name'])         #2d lists

