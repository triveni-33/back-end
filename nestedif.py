#nested if:
"""
l_user="triveni"
l_pass=1234
username=input("enter username:")
if username==l_user:
    password=int(input("enter password:"))
    if password==l_pass:
        print("login successfull")
    else:
        print("wrong password")
else:
    print("wrong username")"""
"""
college=input("student present at college")
if college=="yes":
    block=input("student present at block")
    if block=="yes":
        floor=input("student present at floor")
        if floor=="yes":
           classs=input("student is in class")
           if classs=="yes":
               
              print("he is in class")
           else:
            print("he is in floor")
        else:
           print("he is in block")
    else:
        print("he is in college")
else:
    print("he is absent")
 
 """

# checking whether num is div by 5=buzz,div by 3=fizz,both=fizz buzz 
"""
for i in range(1, 101):
    if i % 3 == 0:
        if i % 5 == 0:
            print("Fizz Buzz")
        else:
             print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
"""
#checking the greatest between 3 values
"""
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if a != b and b != c and a != c:
    if a > b and a > c:
        print(a)
    elif b > c:
        print(b)
    else:
        print(c)
else:
    print("Numbers are equal")
"""
