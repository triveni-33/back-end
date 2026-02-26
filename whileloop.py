
"""
sum=0
while sum<=10:
   
    sum+=1
print(sum)
"""
#reverse
"""
n=5
i=10
while i>=1:
    print(n, "*", i,"=",n*i)
    i-=1
"""


#26/2 -->
#using for loop ---------
"""
 # 3 values tables untill 20
#+ve
n=int(input("enter a num: "))
for i in range(1,21,1):
    if n==1:
        print("1*" ,i, "=" ,1*i)
    if n==2:
        print("2*" ,i, "=" ,2*i)
    if n==3:
        print("3*" ,i, "=" ,3*i)
"""
"""
#-ve
n=int(input("enter a num: "))
for i in range(20,0,-1):
    if n==1:
        print("1*" ,i, "=" ,1*i)
    if n==2:
        print("2*" ,i, "=" ,2*i)
    if n==3:
        print("3*" ,i, "=" ,3*i)
"""

#using while loop---------
"""

 initialise
 while condition
 increment

note: small value (ex: i=1 , < ,+)
      large value (ex: i=10, > ,-)"""
          
"""
#small value initialisation
n=int(input("enter a number: "))
i=1
while i<=20:
    if n==5:
        print(n, "*", i,"=",n*i)
        i+=1
    if n==2:
        print(n, "*", i,"=",n*i)
        i+=1
    if n==3:
        print(n, "*", i,"=",n*i)
        i+=1
"""
"""
#large value initialisation
n=int(input("enter a number: "))
i=20
while i>=1:
    if n==5:
        print(n, "*", i,"=",n*i)
        i-=1
    if n==2:
        print(n, "*", i,"=",n*i)
        i-=1
    if n==3:
        print(n, "*", i,"=",n*i)
        i-=1
"""
#------------------------------------------------------------------------------------
# sum of even and odd numbers
#for loop:---------------
#+ve
"""
even=0
odd=0
for i in range(1,11):
        if i%2==0:
            even=even+i
        else:
            odd=odd+i
print(even)
print(odd)
"""
#-ve
"""
even=0
odd=0
for i in range(10,0,-1):
        if i%2==0:
            even=even+i
        else:
            odd=odd+i
print(even)
print(odd)
"""
#while loop-------------
"""
even = 0
odd = 0

i=1
while i<=10:
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
    i = i + 1

print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)
"""
#reverse
"""
even = 0
odd = 0

i=10
while i>=1:
    if i % 2 == 0:
        even = even + i
    else:
        odd = odd + i
    i = i - 1

print("Sum of even numbers:", even)
print("Sum of odd numbers:", odd)
"""
#print only the numbers that are not divisible by 3
#for loop------
#+ve
"""
for i in range(1, 11):
    if  i % 3 == 0:
        print("_", end=" ")
    else:
        print(i, end=" ")
"""
#-ve
"""
for i in range(10, 0,-1):
    if  i % 3 == 0:
        print("_", end=" ")
    else:
        print(i, end=" ")
"""
#while loop--------
#+ve
"""
i = 1
while i <= 10:
    if  i % 3 == 0:
        print("_", end=" ")
    else:
        print(i, end=" ")
    i = i + 1
"""
#-ve
"""
i = 10
while i >= 1:
    if  i % 3 == 0:
        print("_", end=" ")
    else:
        print(i, end=" ")
    i = i - 1
"""






            





    
    
        
  
        
    
