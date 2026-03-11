#python-heterogenous datatype
"""
x=[1,2,3,4,5,"john"]#end of list will be added
print(x.append(10))
print(x)

x.extend([1,2,3,4,5])#group of elements at a time
print(x)

x.insert(2,"tru")# add at a particular index
print(x)
"""
"""
a=[1,2,3,4]
b=a
print(a)
print(b)
a.append(99)
print("append")
print(a)
print(b))"""

"""
a=[1,2,3,4,99]
print(a.pop(1:3))
#index dwara remove
print(a)
a.remove(99)
print(a)"""

a=[10.2,3,4,99,1]
print(len(a))
print(min(a))
print(max(a))
del(a[1:2])
print(a)

a.sort(reverse=True)
print(a)
b=[10,1,8,3,2]
print(sorted(b))
print(b)

