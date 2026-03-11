"""x=[[1,2],[3,4],[5,6]]
res=[]
for i in x:
    for j in i:
        res.append(j)
print(res)"""
#tuple
t=(1,2,3,4,5,6,1,2,1)
"""
print(t[5])
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sorted(t))
print(id(t))

l=list(t)
print(l)
l.append(99)
print(l)
print(tuple(l))
print(id(l))"""
#set
"""
s={3,5,5,1,2,10,17,8}
print(s)
t={"true",1,1,1,False,0}
print(t)
s.add((99,88,77))#add=tuple
s.update({99,88,77})#update==set,tuple,list
print(s)
"""
"""
s1={True,1,1,1,False,0}

s1.updare({88,7})
print(s1)
print(s1.pop())
print(S1)
"""
kohli={"triveni","sathvik","koti","pardhu"}
dhoni={"tiger","chintu","sathvik","koti"}
#union
print(kohli.union(dhoni))
print(kohli|dhoni)

#intersection
print(kohli.intersection(dhoni))
print(kohli & dhoni)

#difference
print(kohli.difference(dhoni))
print(kohli-dhoni)

#symmetric difference
print(kohli.symmetric_difference(dhoni))
print(kohli ^ dhoni)



