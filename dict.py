"""a={"course":"python","institute":"codegnan",1:"python",1:"java"}
print(a)

#access single value
print(a)
print(a["course"])
print(a["institute"])
print(a[1])
#accessing using keys and values
print(a.get("course","element not found"))
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
print(a.keys())
print(a.values())"""

a={}
print(a)
a.update({1:"tri",2:"veni"})
a.update({3:"chinu"})
print(a)
print(a.pop(3))
a.popitem()
print(a)

a.setdefault(1,"john")
print(a)
a.setdefault(1,"kumar")
print(a)

b=a.copy()
print(b)




