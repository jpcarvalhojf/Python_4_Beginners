import datetime

#INPUT AND PRINT
'''
age = 20
name = 'João'
price = 100.65
is_online = False
'''
'''
user_name = input("What's your name? ")

print("Hello " + user_name)
'''

#CONVERSION TYPES
'''
float()
int()
str()
bool()
'''

#GET CURRENT DATE CALC THE AGE
'''
birth_year = input("Let get your age! \n Tell me your birth year: ")

today = datetime.date.today()

current_year = today.year

age = current_year - int(birth_year)

print("Your age is "+ str(age))
'''

#CONVERT INPUT TO FLOAT
'''
value1 = float(input("First "))
value2 = float(input("Second "))

sum = value1 + value2

print("Total: " + str(sum))

'''

#STRING FUNCTIONS
'''
course = 'Python for Beginners'
#print(course.upper())
#print(course.lower())
#print(course.find('y'))
#print(course.replace('for', '4'))
print('Pithon' in course)
'''

#ARITHMETIC OPERATIONS
'''
variable1 = 3
variable2 = 2

sum = variable1 + variable2
dif = variable1 - variable2
multi =  variable1 * variable2
div =  variable1 / variable2
divRound =  variable1 // variable2
remain = variable1 % variable2
exponentOperator = variable1 ** variable2

x = 3
x = x + 3
x += 2
x *= 4

print('Sum: ' + str(sum))
print('Diff: ' + str(dif))
print('Mult: ' + str(multi))
print('Div: ' + str(div))
print('DivRound: ' + str(divRound))
print('Exponential: ' + str(exponentOperator))
print('x: ' + str(x))
'''
'''
#COMPARISON OPERATORS
a = 2
b = 7
x = a > b
print("A greater than B: "+ str(x))

y = a < b
print("A less than B: "+ str(y))

z = a != b
print("A different than B: "+ str(z))

k = a >= b
print("A greater or equal than B: "+ str(k))

k = a <= b
print("A less or equal than B: "+ str(k))

w = a == b
print("A equal B: "+ str(w))
'''

#LOGICAL OPERATORS
'''
price = 25
print('Value of price is 25. Is price greater than 10? '+ str(price > 10))
print('Value of price is 25. Is price is less than 5? '+ str(price < 5 ))
print('Value of price is 25. Is price between 15 and 30? '+ str(price > 15 and price < 30 ))
print('Value of price is 25. Is price greater than 15 or less than 5? '+ str(price > 15 or price < 5 ))
print('Value of price is 25. Is price not greater than 15 or less than 5? '+ str(not (price > 15) or (price < 5) ))
'''

#IF STATEMENTS
'''
height = 1

if height > 1.80:
    print("It's a tall person")
elif height > 1.65: #(1.65,1.80]
    print("It's in avarage height person")
elif height > 1.50: #(1.50, 1.65]
    print("It's short person")
else:
    print("The height is: "+ str(height) +"."+"\nIF the age between 0 and 10 years ok. Else proceed to medical evaluation")
print("Done")

'''
#EXERCISE
#READ WEIGHT AND UNIT OF MEASUREMENT AND CONVERT TO OTHER Kg or Pounds Lbs
'''
sWeight = input("Please Insert your weight: ")
sWeight = sWeight.replace(',','.')

#checking if a valid weight number input
containCaracters =any(c.isalpha() for c in sWeight)

if containCaracters:
    print("Weight incorrect only numbers is accepted sample: 75.9")
else:
    weight = float(sWeight)

    #checking if a valid UnitMeasurement input
    unitMeasurement = input("Is in Kg or Lbs? \nPress (K) to Kg or (L) to Lbs: ")
    unitMeasurement = unitMeasurement.upper()

    if unitMeasurement != "K" and unitMeasurement != "L":
        print("Unit of Measurement incorrect, please type K or L")
    else:
        if unitMeasurement == "K":
            weightInPounds = weight*2.2
            print("Your weight in Lbs is: "+ str(weightInPounds))
        elif unitMeasurement == "L":
            weightInKilograms = weight/2.2
            print("Your weight in Kg is: "+ str(weightInKilograms))
'''

#WHILE LOOPS
'''
i = 1
#using 1_000 to identify better the number 1000
#in print fuction we can multiply a number with caracter 
while i <= 1_050:
    print(i * '!')
    i += 1
'''

#LISTS
'''
names = ['Terezinha','Kelly', 'Miguel', 'Joao', 'Caco']
# print the entire list
print(names)
# print the first name
print(names[0])
#print the last name
print(names[-1])
#print the second element from the end of the list
print(names[-2])

# changing index item
names[-1] = 'Viva'
print(names)

# printing a range use list[i,n] where python will not consider the element on position n
print(names[0:3])
'''

#LISTS METHODS
'''
numbers = [1, 2, 3, 4, 5]
# insert one item at end of list
numbers.append(6)
print(numbers)

# insert an element where you want
numbers.insert(3,'RAPOSO')
print(numbers)

# remove specific item
numbers.remove(5)
print(numbers)

#return boolean expression if an item is on list
print(4 in numbers)

# len funcition return how many elements on the list
totalElements = len(numbers)
print(totalElements)

#remove all itens
numbers.clear()
print(numbers)
'''

#FOR LOOPS
'''
names = ['JOAO', 'MIGUEL', 'TEREZINHA', 'CACO', 'KELLY']

for item in names:
    print(item)
'''

#RANGE FUNCTION
#It's a built in function that returns a range object
#RANGE will discard the last number on range
'''
numbers = range(5000, 5005)
print(numbers) #will print the range object

for number in numbers:#print all elements in range object
    print(number)
#using incremental step
numbersIncrementalStep = range(5001,5009,3)
for numberIncremented in numbersIncrementalStep:
    print(numberIncremented)

#instead store in variables use the function on for statement
for number in range(2,17,2):
    print(number)
'''

# TUPLES


