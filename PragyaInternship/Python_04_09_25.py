import numpy as np
a = 5
print(type(a))
d ="pragya"
print(type(d))
e={"Name":"Pragya","Class":"Nursery"}
print(type(e))
d=(5,8,9)
print(type(d))
# Operators
# Arithmetic Operators
a = 89
b = 90
print("Sum: ", a+b)
print("Sub: ", a-b)
print("Mul: ", a*b)
print("Div: ", a/b)
print("Floor Div: ", a//b)
print("Mod: ", a%b)
print("Power: ", a**b)
a =5
b = 2
print(a//2)
# assignment operator
a =60
b = 30
print(a ==b)
# comparison operator
a = 60
b = 30
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a <= b)
# logical operator
a1 = True
b1 = True
print(a and b)
a=10
b=12
if a == 10 and b == 12:
    print("true")
else:
    print("false")
if a == 10 or b == 22:
    print("true")
else:
    print("false")
# Bitwise Operator &, etc..
a = 10
b = 4
print(bin(a))
print(a & b)
print(a | b)
x = 5   # 101
y = 3   # 011
result = x & y  # 001
print(result)

x = 5   # 101
y = 3   # 011
result = x ^ y  # 110
print(result)
age = 15
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
marks = 60
if marks >= 80:
    print("Grade a")
elif marks >= 75:
    print("grade b")
elif marks >= 60:
    print("Grade C")
else:
    print("fail")
age = 18
voter = 1
if age >= 18:
    if voter ==1:
        print("Eligible to Vote")
    else:
        print("Not Eligible")
else:
    print("Not Eligible")
count = 1
while count <= 10:
    print(count)
    count += 1
for i in range(10):
    if i == 5:
        break
    print(i)
#* `pass` statement ka use karna hai jab hum koi action nahi lena chahte hain.
# `continue` statement ka use karna hai jab hum current iteration ko skip karna chahte hain.
for i in range(10):
    if i == 5:
        pass
    print(i)
for i in range(10):
    if i == 5:
        continue
    print(i)
#functions
def sum(a,b):
    return a+b
print(sum(98,25))
def fec(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n *fec(n-1)
print(fec(5))
def student(**kwargs):
    print("details:", kwargs)
    for i, j in kwargs.items():
        print(i, ":",j)
print(student(name ="Pragya", age = 25))
a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.ndim)
print(a.shape)
b = np.array([1,2,3], ndmin = 5)
print(b)
print(b.shape)
print(b.ndim)
print(b.dtype)
e = np.array([[1,2,3],[5,6.0,8]])
print(e)
print(e.dtype)
print(e.astype('int'))