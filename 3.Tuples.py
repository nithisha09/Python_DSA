print("Creation")
a = tuple("Nisha")
print(a)
i = 'a','b','c','d'
t = (1,2,3,4,5,5)
print(i,t)
j = ('a',)
print(j)


print("**************")
print("Accessing")
print(a[0])
print(a[1:3])

print("**************")
print("Traverse")
def traverse(t):
    for i in t:
        print(i)
traverse(t)

print("**************")
print("Search")
print('j' in a)
def search(t,v):
    for i in range(len(t)):
        if t[i] == v:
            return f"Element found at {i} position"
    return -1
print(search(a,'s'))
print(a.index("s"))

print("**************")
print("Operations/Functions")
print(a+t)
print(a*2)
print(t.count(5))
print(t.index(5))
print(len(t))
print(max(t))
print(min(t))
print(tuple([1,6,7,8,8]))


print("**************")
print("Deletion")
del a
# print(a) -> error

init_tuple_a = 1, 2
init_tuple_b = (3, 4)
[print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

