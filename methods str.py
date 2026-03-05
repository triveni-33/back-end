"""
x="chintu"
for i in x:
    print(i)
"""
    
"""
y="triveni"
u=""
for i in y:
    u=u+i
print(u.upper())
"""

"""
x=input().upper()
print(x)

u=""
for i in x:
    u=u+i
print(u.upper())
"""

# to get o/p:SPU,am in iterbale for
"""x="SamPU"
for i in x:
    if i.isupper():
        print(i,end="")"""
"""y="SamPU"
for i in y:
    if i.islower():
        print(i,end="")"""
#-----------------------------------------

#to get o/p:SPU,am in range for
"""x="SamPU"
U=""
L=""
for i in range(len(x)):
    if x[i].isupper():
        U+=x[i]
    else:
        L+=x[i]
print(U)
print(L)"""

#-------------------------------------
#using while - to convert upper to low and low to uper without swapcase
"""x="SamPU"
#print(x.swapcase())
s=""
i=0
while i<len(x):
    #print(x[i])
    if x[i].islower():
        s+=x[i].upper()
    else:
        s+=x[i].lower()
    i+=1
print(s)
        """
#--------------------------------
#function
def Add(a,b):
    print(a+b)

Add(10,20)
Add(30,20)
        
        

        

        
