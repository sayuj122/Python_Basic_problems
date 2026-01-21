#1. Given a string, find the longest word. If multiple, print the first.
'''
str1=input("Enter the String:").split()
max=0
for ele in str1:
    if len(ele) > max:
        max=len(ele)
        word=ele
print(word)
'''
#-----------------------------------------------------------
#2. Given a matrix, find the sum of both diagonals.
'''
matrix=[]
size=int(input("Enter the Size of the matrix:"))

for i in range(size):
    row=list(map(int,input(f"Enter the Elements {i+1} in the matrix:\t").split()))
    matrix.append(row)

print(len(matrix))
primary_sum=0
secondary_sum=0

for i in range(size):
    primary_sum += matrix[i][i]
    secondary_sum += matrix[size-1-i][i]

print(primary_sum)
print(secondary_sum)
'''

#3. Read a sentence, count how many are words are strings and how many words are
#numbers.
'''
str1=input("Enter the string:").split()
lenstr1=len(str1)
wordcount=0
numcount=0
for item in str1:
    if item.isdigit():
        numcount += 1
    else:
        wordcount+= 1
print(wordcount)
print(numcount)

'''
#4.Given a string, remove duplicate characters while preserving order.
'''
str1=input("Enter a String:")
result=""
for char in str1:
    if char not in result:
        result +=char
print(result)

'''
#5.Given an array, find the sum of elements at prime indices.
'''
import math

# 1. Initialize variables
n = int(input("Enter the size of the Array: "))
Array = []
prime_sum = 0

# 2. Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

# 3. Input elements into the array
for i in range(n):
    element = int(input(f"Enter element for index {i}: "))
    Array.append(element)

# 4. Calculate sum of elements at prime indices
for i in range(n):
    if is_prime(i):
        print(f"Index {i} is prime, adding value: {Array[i]}")
        prime_sum += Array[i]

print("---")
print("Total Sum of Prime indices:", prime_sum)'''
#-------------------------------------------------
#6.Given two strings, check if the second string is a rotation of the first.

'''
def is_rotation(str1, str2):
    # Step 1: Check if lengths are the same
    if len(str1) != len(str2):
        return False
    
    # Step 2: Concatenate str1 with itself
    combined = str1 + str1
    
    # Step 3: Check if str2 is inside the combined string
    if str2 in combined:
        return True
    else:
        return False

# Test the function
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if is_rotation(s1, s2):
    print(f"'{s2}' is a rotation of '{s1}'")
else:
    print(f"'{s2}' is NOT a rotation")

'''
#7.Find first repeating elements in an array.
'''
array=[5,6,8,2,6,5,3]
for x in array:
    if array.count(x)>1:
        print(x)
        break

'''