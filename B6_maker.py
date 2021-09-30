import pyinputplus as pyip

print('hello my world')

#Sandwich maker
cost = 0
totalCost = 0
print('How many sandwiches do you want?: ')
number = pyip.inputInt(min=1)

print('Which bread type would you like to take?')
bread = pyip.inputMenu(['wheat', 'white', 'sourdough'],numbered=True)
if bread == 'wheat':
    cost += 40
elif bread == 'white':
    cost += 90
else:
    cost += 70

print('Which protein type would you like to take?')
protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],numbered=True)
if protein == 'chicken':
    cost += 40
elif protein == 'turkey':
    cost += 90
elif protein == 'ham':
    cost += 80
else:
    cost += 70

print('Would you like cheese?')
cheese = pyip.inputYesNo()
if cheese == 'yes':
    print('Which cheese type would you like to take?')
    cheeseType = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], numbered=True)
    if cheeseType == 'cheddar':
        cost += 40
    elif cheeseType == 'Swiss':
        cost += 90
    else:
        cost += 70

print('Which flavor would you like to take?')
flavor = pyip.inputMenu(['mayo', 'mustard', 'lettuce', 'tomato'],numbered=True)
if flavor == 'mayo':
    cost += 40
elif flavor == 'mustard':
    cost += 90
elif flavor == 'leyyuce':
    cost += 80
else:
    cost += 70


totalCost = number * cost
print(f'You have ordered {number} sandwiches with totalcost:{totalCost}$')
