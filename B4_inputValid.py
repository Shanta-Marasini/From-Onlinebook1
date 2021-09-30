import pyinputplus as py
print('hello Shiva baba my world')

print('enter a number:')
age = py.inputInt(min=1,lessThan=125,blank=True,limit=2,timeout=10,default='N/A')
print(age)
#help(py.inputChoice)  provides informaton about this function


#regular expressions for input valid
#allowRegexes,blockregexes
print('enter age age:')
num = py.inputInt(allowRegexes=[r'(I|V|X|L)'])

#doesnot accept even numbers
print('enter odd number')
odd = py.inputInt(blockRegexes=[r'[02468]$'])

#add digits upto 10

def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.' %(sum(numbersList)))
    return int(numbers)

print('enter digits')
response = py.inputCustom(addsUpToTen)
print(response)