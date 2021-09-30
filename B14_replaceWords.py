import re
from pathlib import Path
print('Hello my world')


fileObj = open('text.txt','r')
# wr = fileObj.write('The ADJECTIVE panda walked to the NOUN and then VERB./'
#               ' A nearby NOUN was unaffected by these events.')

fileText = fileObj.read()
replaceWords = fileText
#find words through regexes
findWords = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')
matchWords = findWords.findall(fileText)
print(matchWords)

#user input
if len(matchWords) != 0:
    for word in matchWords:
        if word == 'ADJECTIVE':
            print('enter an adjective: ')
            adj = input()
            replaceWords = re.sub('ADJECTIVE', adj, replaceWords,1)

        elif word == 'NOUN':
            print('enter a noun : ')
            noun = input()
            replaceWords = re.sub('NOUN', noun, replaceWords, 1)

        elif word == 'VERB':
            print('enter a verb : ')
            verb = input()
            replaceWords = re.sub('VERB', verb, replaceWords, 1)

        else:
            print('enter an adverb : ')
            adverb = input()
            replaceWords = re.sub('ADVERB', adverb, replaceWordse, 1)

print(replaceWords)

# newFile = open('new.txt','r')
# newFile.write(fileText)
#
# newFile.read()

