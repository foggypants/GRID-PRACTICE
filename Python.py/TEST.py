'''
import math
print(int(math.sqrt(25)))
print(int(math.pow(5,2)))
print(math.pi)
print(math.ceil(4.001))
print(math.floor(4.7))
'''
'''
import datetime
print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)

import random
print(random.randint(1,10))
print(int(random.random()))
print(random.choice(['apple', 'banana', 'cherry']))
cards=['2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING','ACE']
random.shuffle(cards)
print(cards)
print(random.sample(cards,5))
print(random.uniform(1.5,10.5))
print(random.randrange(0,101))

import mymodule as x
b=x.a['age']
print("Age:",b)


x=10
try:
    print(x)

except NameError:
    print("Variable x is not defined")
else:
    print("No Error")

finally:
    print("Execution completed")


try:
    f=close("non_existent_file.txt","w")
    try:
        f.write("hello world")
    except:
        print("An error occurred while writing to the file.")
    finally:
        f.close()
except:
    print("An error occurred while handling the file.")


x=24
if not type(x) is int:
    raise TypeError("Variable x is not an integer")
else:
    print("x is an integer")

f=open("/Users/foggypants/Desktop/xyz/non_existent_file.txt","w")
f.write("\nHello,World!\nHI THERE!\nBYE NOW!\n")
f.close()

f=open("/Users/foggypants/Desktop/xyz/non_existent_file.txt","r")
print(f.read())
f.close()

print(max("a,z,z"))

print({1,2,3}|{3,4,5,6})


square=lambda x, y: x*y
print(square(5,3))
nums=[1,2,3,4,5,6,7,8,9,10]
result=list(map(lambda x: x*2, nums))
print(result)
filtered=list(filter(lambda x: x%2==0, nums))
print(filtered)
students=[('John',85),('Jane',92),('Dave',78),('Sara',90)]
students.sort(key=lambda x: x[1], reverse=True)
print(students)

def decorator(func):
    def wrapper():
        func()
        print("Before function execution")
        func()
        print("After function execution")
        func()
    return wrapper
@decorator
def say_hello():
    print("Hello!")
say_hello()
'''


def login():
    username=input("Enter username: ")
    password=input("Enter password: ")
    if username=="admin" and password=="password123":
        print("Login successful!")
    else:
        raise ValueError("Invalid username or password")
try:
    login()
except ValueError as ve:    
    print(ve)
def user():
    # define a local helper function before calling it
    def func():
        pass
    func()
    print("User function executed")
try:
    user()
except NameError as ne:
    print("Error:",ne)

