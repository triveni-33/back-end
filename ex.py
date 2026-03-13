#printing keys where values less than 50
"""
a={"duhi":31,"josh":41,"jimin":90,"hoshi":56,"romi":33}
less=[]
great=[]
for key,val in a.items():
    if val>50:
        great.append(key)
    else:
        less.append(key)
print(great,less)
"""

#printing only middle values -2,4,6
#possiblity1
"""
a = {'a':[1,2,3], 'b':[3,4,5], 'd':[5,6,7]}
for i in a.values():
    print(i[::2])
#possibility2
x= {'a':[1,2,3], 'b':[3,4,5], 'd':[5,6,7]}
l=[]
for val in x.values():
    
    for j in range(len(val)):
        if j%2==0:
            l.append(val[j])
print(l)
"""

##printing how many times the alphabet is taken in dict pattern
#not in
"""
s="aabbcc"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
#in
s="aabbcc"
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
"""
#reverse dic key,values
#pos-1
"""
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
new= {}
for i,j in d.items():
    new.update({j:i})
print(new)

#pos-2
for k,v in d.items():
    new[v]=k
print(new)

#pos-3
y={v:k for k,v in d.items()}
print(y)
"""

x = "abcaadd"

d = {}

for ch in x:
    d[ch] = d.get(ch, 0) + 1
    
    if d[ch] == 1 and ch != 'd':
        print(ch + "1", end=" ")
    elif d[ch] == 2:
        print(ch + "2", end=" ")

