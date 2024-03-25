import array 
import numpy
"""
#############################################################################
                # 1D ARRAY
#############################################################################
# Creation
a = array.array('i')
print(a)
b = array.array('i', [1,2,3,4])
print(b)

c = numpy.array([],dtype=int)
print(c)
d = numpy.array([9,5,3,0,1])
print(d)

print("*********************")
print("Insertion")
i = array.array('i', [5,6,7,8])
i.insert(0,1)
i.insert(3,9)
i.insert(6,10)
i.insert(11,100)
print(i) #[1, 5, 6, 9, 7, 8, 10, 100]

print("*********************")
print("Traversal")
def traversal(arr):
    for i in arr:
        print(i)
traversal(i)

print("*********************")
print("Accessing")
def access(arr,i):
    if i>=len(arr):
        print("Index out of range")
    else:
        print(arr[i])
access(array.array('i',[11,12,13,14,15]),3)

print("*********************")
print("Searching")
def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return f"Element found at {i} index position"
    return -1
print(search(array.array('i',[11,12,13,14,15]),1))

print("*********************")
print("Deleting")
def remove(arr,x):
    if x in arr:
        arr.remove(x)  #deletes first occurance
        print(arr)
    else:
        print("Element not present")
remove(array.array('i',[11,12,13,14,15]),11)

print("*********************")
print("Append")
k = array.array('i',[1,2,3,4,5])
k.append(10)
print(k)

print("*********************")
print("Extend")
k.extend([11,12,13])
k.extend(array.array('i',[20,21,22]))
print(k)

print("*********************")
print("Create array from List")
p = array.array('i')
l = [9,3,7,5,8]
p.fromlist(l)
print(p)

print("*********************")
print("Pop")
p.pop()
print(p)

print("*********************")
print("Finding Index of any given value")
s = array.array('i',[11,11,2,45,5])
print(s.index(11))

print("*********************")
print("Reverse")
s.reverse()
print(s)

print("*********************")
print("Buffer Info")
print(s.buffer_info())

print("*********************")
print("Count Occurences of a number")
print(s.count(11))

print("*********************")
print("Array to String")
str = s.tobytes()
print(str)
print("Array from String")
arr = array.array('i')
arr.frombytes(str)
print(arr)

print("*********************")
print("Array to List")
print(arr.tolist())

print("*********************")
print("Slicing")
ar = array.array('i',[1,2,3,4,5,5,6])
print(ar[1:4])
print(ar[-6:-3])
"""
#############################################################################
                # 2D ARRAY
#############################################################################

print("*********************")
print("Creation")
twod = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(twod)

print("*********************")
print("Insertion")
newArray = numpy.insert(twod,2, [[0,0,0]],axis=0) #axis 1-> col; 0->row
print(newArray)

print("*********************")
print("Append")
appendArray = numpy.append(twod,[[0,0,0]],axis=0)
print(appendArray)

print("*********************")
print("Access")
def accessing(arr,r,c):
    if r>=len(arr) or c>=len(arr[0]):
        print("Index out of range")
    else:
        print(twod[r][c])
accessing(twod,2,2)

print("*********************")
print("Traversal")
def trav(arr):
    for i in arr:
        for j in i:
            print(j)
trav(twod)

print("*********************")
print("Searching")
def searching(arr,x):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==x:
                return f"Element found at {i},{j} index position"
    return -1
print(searching(twod,8))

print("*********************")
print("Deletion")
newArr = numpy.delete(twod,1,axis=0)
print(newArr)