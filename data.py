#Data Types
#Numbers 1,2,3
""" def add(x,y):
    print(x + y)
add(1,2)
#strings "a,b,c"
name = "Mark"
def greeting(person):
    print(person)
greeting(name) 
#1 and "1" are not the same
add("1","2")
#undefined/null

#booleans
tenure = False
def is_tenure(status):
    if(status == True):
        print("They have tenure")
    else:
        print("They are not tenured")
    
is_tenure(tenure)
 """
""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i)

print(values[0])
print(values[6]) """

""" x = "this is a thing"
y= x.split( )
z = y[0]
print(y)
print(z) """

""" day_of_week = input("what day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}")

temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold') """


#EVEN ODD
""" x = 0 
x = float(input("give me a number"))
if x% 2 == 0: 
    print('even')

else:
    print('odd')  """


#Word Counter
""" x = input()
numberletters = x.split( )
print(len(numberletters)) """


#Tip Calculator
""" y = float(input("How much was you bill"))
x = input("How was your service")

total = y 

if x == "bad":
    print('0% tip')
    total = total * 1.0
    print(total)
    
elif x == "okay":
    print('15% tip')
    total = total * 1.15
    print(total)

elif x == "good":
    print('20% tip')
    total = total * 1.2
    print(total)

elif x == "great":
    print('25% tip')
    total = total * 1.25
    print(total) """


#Factor finder
""" x = float(input("Give me a number"))
x == int(x)

factors = []

for i in range(1,int(x/2)):
    if x%i == 0:
        if i not in factors: 
            factors.append(i)
        if x/i not in factors:
            factors.append(int(x/i))

for i in factors:
    print(i) """

#GCF (imported math)

""" import math
from math import * 

x = int(input("give me a number"))
y = int(input("give me another number"))

number = gcd(x,y)
print(f"{number}") """


#GCF
x = int(input("Give me a number"))
y = int(input("Give me another number"))
list_factors = []
z = 1

def factor():
    if x > y: 
        z = x 
    elif x < y:
        z = y 
    for i in range(1, z+1):
        if x%i == 0 and y%i == 0:
            list_factors.append(i)
    print(max(list_factors))
factor()


