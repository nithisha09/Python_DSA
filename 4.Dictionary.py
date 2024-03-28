print("Creation")
a = dict() #a = {}
print(a)

a={"Nithisha": 24, "Chandru": 23, "Tom": 10}
dic = dict(one= 1, two= 2, three= 3)
print(a,dic)

# Using List
l = [("Nithisha", 24),("Chandru", 23),("Tom", 10)]
d = dict(l)
print(d)

print("************")
print("Update/Insert")
a["Nithisha"] = 25
print(a)
a["Jerry"] = 5
print(a)

print("************")
print("Traverse")
def traverse(d):
    for k,v in a.items():
        print(k,v)
traverse(a)

print("************")
print("Search")
def search(d,x):
    for k,v in a.items():
        if v==x:
            return f"{k}:{v}"
    return "Value doesn't exist"
print(search(a,100))

print("************")
print("Deletion")
del a["Jerry"]
print(a)
a.pop("Tom")
print(a)
print(a.popitem())
a.clear()
print(a)

print("************")
print("Methods")
f = dict(o=0,g=9)
f.clear()
print(f)
f = dict(o=0,g=9)
g = f.copy()
print(g)
f["o"]=8
print(f,g)

p = {}.fromkeys([1,2,3],"Hi")
print(p)

print(p.get(4,"No present"))
print(p.items())
print(p.keys())
print("#####################")
p.setdefault(4,"Bye")
p.setdefault(3,"Bye")
print(p)
b = p.pop(5,"Not present")
print(b)
print(p.values())
j = {1:"Byebye", 9: "HiHi", 10: "Goodnight"}
p.update(j)
print(p)

print("************")
print("Operations/Built in Functions")
print("Byebye" in p.values())
print(len(p))
print(all(p))
print(any(p))
print(sorted(p))

print("************")
print("Dict Comprehension")
city = ['a','b','c','d','e']
fruit = {"Apple":100,"Orange": 50,"Banana":30}
new_dict = {i:"Hello" for i in city}
print(new_dict)
fruit_dict = {k:v for k,v in fruit.items()}
print(fruit_dict)
if_fruit_dict = {k:v for k,v in fruit.items() if k=="Orange"}
print(if_fruit_dict)
