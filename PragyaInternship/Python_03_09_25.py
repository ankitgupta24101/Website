print("Hello World")
# Data Type
# Variable don't start with number,special character.
# Variable always start with underscore and alphabet
# Cannot use reserved keyword in naming
x = 14
print(type(x))  # Check data type of variable
y = "hello"
print(type(y))
a = 5
b = 6
sum = a + b
print(sum)
x = 20
if x < 15:
    print("x is lesser than 15")
else:
    print("x is greater than 15")
age = 28
if age >= 18:
    print("Eligible to Vote")
    if age >= 60:
        print("You are also a Senior Citizen")
    else:
        print("You are not a Senior Citizen")
else:
    print("Not Eligible to Vote")

for i in range(10):
    if i % 2 == 0:
        print(i)

x = 0
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")
i = 0
# for i in range(start, end, step):
for i in range(1, 10, 2):
    print(i)
for i in range(1, 6):
    print("Chocolate given to student {i}")
    # for printing value of i
    print(f"Chocolate given to student {i}")
count = 1
while count <= 5:
    print(count)
    count += 1

for row in range(1,4):
    for col in range(1,4):
        print(f"Seat => row: {row}, col: {col}")
for i in range(4):
    for j in range(3):
        print(i,j)