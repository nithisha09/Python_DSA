# Creation
a = [1,2,3,4,5]
b = ['Apple','Orange', 'Mango','Banana']
c = [1,1.5,'Choco',[1,2,3]]
d = []
print(a,b,c,d)

print("*******************")
print("Accessing/Traversal")
print(b[1])
print(c[-1])
print("Banana" in b)
for i in range(len(b)):
    print(b[i])

print("*******************")
print("Update/Insert")
i = ['Apple','Orange', 'Mango','Banana']
i[1] = "Plums"
# i[6]="K" -> error
i.insert(3,'Strawberry')
i.insert(5,[2,2,4,1])
i.append(100)
i.append([199,300])
i.extend([1,1,1,1,1])
print(i)

print("*******************")
print("Slice/Delete")
k = [1,2,3,4,5,5,6,7,8,9]
print(k[0:2])
k[0:2] = ['x','y']
print(k)
k.pop(0)
del k[0:3]
k.remove(5)
print(k)

print("*******************")
print("Search")
t = [1,2,3,4,5,5,6,7,8,9]
def search(l,x):
    if x in l:
        return "Element is present"
    return "Element not present"
print(search(t,100))

def searchIndex(l,x):
    for i,val in enumerate(l):
        if val==x:
            return i
    return -1
print(searchIndex(t,5))

print("*******************")
print("Operaions/Functions")
m = [1,2]
n = [0,4]
o = m+n
print(o)
print(o*2)
print(len(m))
print(max(m))
print(min(m))
print(sum(m))

# Game1
"""
p = list()
while(True):
    # ip = 3
    ip = input("Enter a number")
    if ip == "done":
        break
    p.append(float(ip))
print(p)
avg = sum(p)/len(p)
print(f"Average is {avg}")
"""

print("*******************")
print("Lists and Strings")
x = "Nisha"
y = list(x)
print(y)
x = "Nisha Nisha Nisha"
print(x.split())
x = "Nisha/Nisha/Nisha"
print(x.split("/"))
v =['1','2','3','4']
print("-".join(v))

print("*******************")
print("List Comprehension")
f = [1,2,3,4,5,6]
g = [i/2 for i in f]
print(g)
lang = "Python"
letters = [i for i in lang]
print(letters)

z = [1,2,3,4,5,6]
even = [i*2 for i in z if i%2==0]
print(even)

name= "Nisha1"
vowels = 'aeiou'
cons = [i for i in name if i not in vowels and i.isalpha() ]
print(cons)

ifcond = [i*5 if i==5 else 0 for i in z]
print(ifcond)






