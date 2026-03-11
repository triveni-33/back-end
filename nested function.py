#nested function
"""def Home():
    n=input("enter name")
    def Profile():
        print("i sleep",n)
    print("iam")
    Profile()
Home()"""
"""
def Calculator(a,b):
    def Add():
        a=10
        b=20
        print(a+b)
    print("i ")
    def Sub():
        print(x-y)
    
    print("iam fon")
    Sub()
    
x=10
y=20
Calculator(x,y)
   
#Calculator(5,8)"""
"""
def recur(x):
    for i in range(x):
    print(x)
recur(5)"""
"""
def recur(x):
    if x!=0:
        print(x)
        recur(x-1)
recur(5)"""
"""
def table(n, i):
    if i > 10:   # stopping condition
        return
    print(n, "x", i, "=", n*i)
    table(n, i+1)   # recursive call

num = int(input("Enter number: "))
table(num, 1)"""
"""
def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

num = int(input("Enter number: "))
table(num)"""
"""
def table(n, i):
    if i > 10:
        return
    print(n, "x", i, "=", n*i)
    table(n, i+1)

table(5,1)

print("Reverse Table")

def table_rev(n, i):
    if i == 0:
        return
    print(n, "x", i, "=", n*i)
    table_rev(n, i-1)

table(5,10)
"""
"""
def Fib(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
Fib(5)"""


def Fib(n):
    if n<=1:
        return n
    return Fib(n-1)+Fib(n-2)
    
print(Fib(4))

