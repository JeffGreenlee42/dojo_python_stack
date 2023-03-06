num1 = 42 # variable declaration and initialization - in this case an Int Number
num2 = 2.3 # variable declaration and initialization - in this case a float Number
boolean = True  # variable declaration  and initialization- a boolean
string = 'Hello World' # variable declaration and initialization - a string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #Variable declaration and initialization of a list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #Variable declaration and initialization of a dictionary
fruit = ('blueberry', 'strawberry', 'banana') #Variable declaration and initialization of a tuple with 3 elements
print(type(fruit)) # log statement - type check
print(pizza_toppings[1])   # access value of list
pizza_toppings.append('Mushrooms') # list - add value
print(person['name']) # dictionary - access value
person['name'] = 'George' # dictionary - Change vlue
person['eye_color'] = 'blue' # dictionary - add value 
print(fruit[2]) # log statement - Tuple alccess value

if num1 > 45:  # if
    print("It's greater") # log statement
else:  # else
    print("It's lower") #log statement

if len(string) < 5:  # if - length check
    print("It's a short word!") # log statement (string)
elif len(string) > 15: # else if - length check
    print("It's a long word!")  # log statement (string)
else:  #else
    print("Just right!")  #  log statement (string)

for x in range(5):  # for loop increment
    print(x) # log statement (for index)
for x in range(2,5): # for loop increment
    print(x)  # log statement
for x in range(2,10,3):  # for loop increment
    print(x)  # log statement
x = 0 #  declare and initialize global number variable
while(x < 5): # while loop
    print(x)  # log statement 
    x += 1 # increment number value

pizza_toppings.pop()  # list delete value
pizza_toppings.pop(1) #  list delete 2nd value

print(person)  # log statement (whole dictionary)
person.pop('eye_color') # delete dictionary key-value pair
print(person) # log statement (dictionary instance now has viewer entries)

for topping in pizza_toppings:  # for loop
    if topping == 'Pepperoni': # if  statement if item exists
        continue  #  don't do anything in this loop.. advance to next item in loop
    print('After 1st if statement') #log statement 
    if topping == 'Olives':  # if statement if item exists
        break # exit loop

def print_hello_ten_times():  # function declaration
    for num in range(10):  # for loop 
        print('Hello')  # log statement (string)

print_hello_ten_times()  # call function

def print_hello_x_times(x):  # Function declaration - one passed in variable
    for num in range(x):  # for loop 
        print('Hello')  # log statement (string)

print_hello_x_times(4)  # call function with passed value

def print_hello_x_or_ten_times(x = 10): # function declaration
    for num in range(x):  # for loop
        print('Hello') # log statement (string)

print_hello_x_or_ten_times()  # call function
print_hello_x_or_ten_times(4) # call function with passed value

# Multi-line comment
"""  
Bonus section
"""

# print(num3)  NameError: name <variable name> is not defined
# num3 = 72  # variable initialization and declaration
# fruit[0] = 'cranberry'  - Tuple - Change value
# print(person['favorite_team'])  - KeyError: 'favorite_team'  
# print(pizza_toppings[7]) - IndexError: list index out of range
#   print(boolean)   - IndentationError: unexpected indent
# fruit.append('raspberry')  - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1)  - AttributeError: 'tuple' object has no attribute 'pop'