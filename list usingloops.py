"""x=[1,2,3,4,5,6,7]
count=0
for i in x:
    if i%2!=0:
        count+=1
print(count)"""
"""
x=[1,2,3,4,5,6,7]

for i in range(len(x)):
    if i%2==0 and x[i]%2!=0:
        print(x[i])
"""
"""
x=[1,2,3,4,5,6,7]
ind=0
for i in x:
    if ind%2==0 and i%2!=0:
        print(i)
    ind=ind+1
"""

a=["PytHON","CYThon","oRACle","MiraCLE"]
lower=0
upper=0
i=0
while i<len(a):
    j=0
    word=a[i]
    while j<len(word):
        if word[j].isupper():
            upper+=1
        else:
            lower+=1
        j+=1
    j=0
    i+=1
print(lower,upper)


    
