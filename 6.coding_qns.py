# Get no. of days as i/p
# Get temperatures as i/p for the no. of days specified in step1 
# Calculate average temperature for the days given
# Find no. of days greater than average temperature

"""
total_days = int(input("Enter no. of days: "))
temp = []
for i in range(total_days):
    t = int(input(f"Enter {i+1}'s day temp: "))
    temp.append(t)
avg = sum(temp)/len(temp)
print(f"Average temperature is {round(avg,2)}")

count=0
for i in temp:
    if i>avg:
        count+=1
print(f"No of Days greater than average temperature: {count}")
"""

# Find the missing number in Array/List
# Given no of items and array
"""
def missing(arr,n):
    sum_of_n = n*(n+1)//2
    return sum_of_n - sum(arr)
print(missing([1,2,3,4,5],6))
"""
# Two Sum - Leetcode
# Given an array of integers nums and an integer target
# return indices of the two numbers such that they add up to target.
"""
    temp = {}
    for i,v in enumerate(nums):
        if target-v in temp:
            return [i,temp[target-v]]
        temp[v] = i
"""
import numpy
arr = numpy.array([1,2,3,4,5,8])

"""
def search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
print(search(arr,4))
"""
# Find the max product of 2 integres in an array
"""
def product_max(arr):
    max1 = 0
    max2 = 0
    for i in arr:
        if i>max2 and i<max1:
            max2 = i
        if i>max1 and i>max2:
            max2 = max1
            max1 = i
    return max1*max2
print(product_max(arr))
"""
# Permutation
"""
l1 = [1,2,3,4,0]
l2 = [3,1,4,2,6]
def permutation(l1,l2):
    if len(l1)!=len(l2):
        return False
    l1.sort()
    l2.sort()
    if l1==l2:
        return True
    return False
print(permutation(l1,l2))
"""
# Rotate matrix by 90 degree clockwise
def rotate(matrix):
    # TODO
    # Find transpose
    for i in range(len(matrix)):
        for j in range(i+1,len(matrix[0])):
            t = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = t
    # Reverse each row
    for i in matrix:
        i.reverse()
    return matrix