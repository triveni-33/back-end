Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=20
c=30
a+b+c
60
10+20+30
60
a-b
-10
B=100
b+B
120
a=100
a+a
200
10//2
5
10/2
5.0
10%2
0
10**2
100
b**2
400
#the above are the arithmetic operators  : //->quotitent,/->quotientdecimal,%->remainder,**->square
a=1
b=2
c=3
a+b-c
0
a+(b-c)
0
#assigment operator :
a=10
a+=2
a
12
a-=10
a=30
a
30
a=10
a*=2
a
20
a=2
a/=10
a
0.2
a=10
a-=1
a
9
a=112
a=11
a*=1
a
11
a=10
a//=2
a
5
#comparision operaiors :
x=99
y=78
x>y
True
x==y
False
x<y
False
x!=y
True
x=10
y=1-
SyntaxError: invalid syntax
y=10
x!=y
False
#logical :
a=100
b=200
a and b
200
0 and 100
0
100 and 0
0
\
age=18
marks=100
age>=18
True
marks<=100
True
age>=18 and marks<=100
True
age>18 and marks<=100
False
age<=18 and marks==100
True
age==17 and marks>99
False
age>10 and marks>100
False
age>=17 and marks<150
True
age>=17 and marks<150 and 100==100
True

age>=17 and marks<150 and 0 and 100
0
age>=17 and marks<150 and 100 and 0
0
age>=17 and marks<150 and True and False
False
True and False and True and 0
False
10 >50
False
10 or 50
10
50 or 10
50
-10 and 50
50
50
50
0 or -1
-1
age>17 or marks>99
True
False or False or False or 0
0
False or False or False or -1
-1
not True
False
not (True and False)
True
