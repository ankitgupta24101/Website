a = [1,5,99,8,72]
b = ["a","b","c"]
c = [1,'a','5.0']
print(a)
print(b)
print(c)
d = [10]* 5
print(d)
f = [10,12,5,89,25]
print(f[1])
print(f[-1])
print(f[0:3:2])
print(f[::-1])
f.append(19)
print(f)
f.extend([2,3,6,4])
print(f)
f.insert(1,50)
print("After Insert => ",f)
f[4] = 400
print("After Update => ",f)
f.remove(400)
print("After Remove => ",f)
f.pop()
print("After Popup => ",f)
del f[2]
print("After Delete => ",f)
f.clear()
print(f)
# list is created
a = []
n = int(input("Enter number of elements : "))
for i in range(n):
    element = int(input("Enter element : "))