n = int(input("Enter Number of steps: "))


count = 4
base =  (5*n) - 1
print(f" {"_" * 4}")
for i in range (1,n):    
    print(f"|{" " * count}|")
    print(f"|{" " * count}|____")
    count += 5

print(f"|{" " * count}|")
print(f"|{"_" * base}|")



"""
if n == 1:
    h = 2
    w = 4
    b = 4
    print(f" {"_" * w}")
    for i in range(h-1):
        print(f"|{" " * w}|")
    print(f"|{"_" * w}|")
else:
"""