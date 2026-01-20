print("Hello World")

# integers and floats

var_a =3.14
print(type(var_a))
#power
print(3**2)

#incrementation
var_b=10
var_c=10
var_b*=10
print (var_b)
var_c+=10
print (var_c)


#built in function in integers
"""The absolute value of a real number is its non-negative value without regard to its sign,"""
print(abs(-3))

#round 
print(round(3.75))
print(round(3.75,1))

#Type casting
var_d=60

var_e=str(var_d)
print(var_d)

#LIST
course=['history','mechanical']
print(course)
print(course[0])
print(len(course))
print(course[0:])
course.append('art')
course.insert(1,'physics')
print(course)

#extend: to join 2 lists

course_2=['civil','maths']
course.extend(course_2)
print(course)

 #pop func in List
course.pop()#pop func remove the last element
course.remove('art')
print(course)

course.reverse()
print(course)

#sort
course.sort()# aplahbetic order for the given exmaple
print(course)
course.sort(reverse=True)

print(course)

