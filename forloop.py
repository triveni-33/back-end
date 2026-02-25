"""
# print * * * * *
        * * * * *
#+ve -->

for i in range(1,3,1):
    print("* "*5)
    
"""
#-ve -->
"""

for i in range(5,1,-2):
    print("*" * 5)
"""



#-----------------------------------
"""
# print 1 1 1
        1 1 1
        1 1 1
#+ve -->
for i in range(1,4,1):
    print("1 " * 3)
"""

#-ve -->
"""
for i in range(15,6,-3):
    print("1 "*3)
"""


#-----------------------------------
#print # #
       # #
"""
#+ve  -->

for i in range(1,3,1):
    print("# "*2)
"""
"""
#-ve -->
#possibility 1      ---

for i in range(4,0,-2):
    print("# " *2)
    
#possibility 2      ---

for i in range(7,3,-2):
    print("# " *2)
    
"""
#-----------------------------------
"""
#print 0 0 0
       0 0 0
       0 0 0
       0 0 0
       0 0 0 """
#ve -->
"""

for i in range(1,6,1):
    print("0 " * 3)
"""
#-ve -->

"""
for i in range(15,0,-3):
    print("0" * 3)
"""

#-----------------------------------
#@ @ @ @ @
#ve -->
"""
#possibility 1  ---

for i in range(1):
    print("@ " * 4)
    
#possibility 2  ---

for i in range(2,3):
    print("@ " * 4)
"""

#-ve -->
"""

for i in range(2,3):
    print("@ " * 4)
"""
#-----------------------------------
# print 3 table
#+ve -->
"""
for i in range(1,11,1):
    print("3*" ,i, "=" ,3*i)
"""
#-ve -->
"""
for i in range(10,0,-1):
        print("3*" ,i, "=" ,3*i)
"""
#-----------------------------------
#print 5 table
#ve -->
"""
for i in range(1,11,1):
        print("5*" ,i, "=" ,5*i)
"""
#-ve -->
"""
for i in range(10,0,-1):
        print("5*" ,i, "=" ,5*i)
"""
#-----------------------------------
#leap years any 10
"""
#+ve
for i in range(2000,2040,4):
    print(i)
"""
"""
#-ve
for i in range(2040,1999,-4):
    print(i)
"""
#----------------------------------


