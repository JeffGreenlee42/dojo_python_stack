#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
# Prediction:  returns 5


#2
def number_of_military_branches():
    return 5
print(7 + number_of_military_branches())
# Prediciton:  prints 12


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
# Prediction:  Prints 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Prediction:  it will print 5 (ignores "print(10)" because that line is improperly indented, and will be circumnavigated by the previous print statement)


#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
# Prediction :  x is defined but is not initialized.   It will print 5 in the function  but x will be undefined.

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#  Prediction:  This may or may not work.  The function does not return anything..  Can it add what it prints?  we may get an error
#  if it works  it will print  8.


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
# # Prediction:  it will print "25"

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
# Prediction:  It will print 100  10   - line #60 return 7 will never execute execute"

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# Prediction:  1)  it will print 7
#              2)  It will print 14
#              3)  It will print 21
#   This function will never return 3

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
# Prediction:  This will print 8   - This function will never return 10

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
# Prediction:   1) it will print 500
#               2) It will print 500
#               3) it is inside function - it will print 300
#               4) Variable b was not declared Global so function won't change it.. it will print 500



#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
# Prediction:  1)  prints 500
#              2)  prints 500
#              3)  Function prints 300 
#              4)  Global b did not change .. it prints 500

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
# Prediction:  1) print 500
#              2) print 500
#              3) print 300
#              4) print 300

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
# Prediction:   1) Print 1
#               2) Print 3
#               3  Print 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
# Prediction:   1) Print 1
#               2) Print 3
#               3) Print 5
#               4) Print 10