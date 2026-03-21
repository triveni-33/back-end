#reduce
"""
from functools  import reduce
x=[1,2,3,5]
print(reduce(lambda a,b:a+b,x))
"""
#all-ani true ayi undali
"""
a=[1,2,3,4,5]
a=[1,2]
result=all(i%2==0 for i in a)
print(result)
"""
#any - okati ayina true avali
"""
a=[1,2,3,4,5]
a=[2,4,6,8]
result=any(i%2==0 for i in a)
print(result)
"""
"""
a=[1,2,3,4]
for i in range(len(a)):
    print(i,a[i])
    """
#enumerate-manam edaite start lo istame adi starting indexlaga tiskunidi
"""
a=[1,2,3,4]
for i,val in enumerate(a,start=2):
    print(i,val)
    """
#list comprehension-
# a=[10,20,30,40]
# even=[]
# for i in a:
#     if i%2==0:
#         even.append(i)
# print(even)
# a=[10,20,30,40,13]
# result=[i for i in a if i%2==0]
# res=[i if i%2==0 else "odd" for i in a]
# print(result)
# print(res)

l=[]
for i in range(3):
    for j in range(3):
        l.append((i,j))
print(l)

l=[]
for i in range(3):
    for j in range(3):
        if i
    

