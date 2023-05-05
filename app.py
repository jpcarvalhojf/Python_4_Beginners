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

#COMPARISON OPERATOS
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
