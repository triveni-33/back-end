#printing the case senstive letters using functions
"""def count(s):
    u=0
    l=0
    for i in s:
        if i.isupper():
            u+=1
        elif i.islower():
            l+=1
    print("Upper:", u)
    print("Lower:", l)

word = input("Enter string: ")
count(word)"""

#reversing a word
"""
def Reverse(word):
    
    rev = ""
    for i in word:
        rev = i + rev
    print(rev)

w = input("Enter word: ")
Reverse(w)
"""


#printing vowels and consonants count in a given word using fun
"""
def vowcon(s):
    v =0
    c = 0
    for i in s:
        if i.lower() in "aeiou":
            v+=1
        elif i.isalpha():
            c+=1
    print("Vowels:", v)
    print("Consonants:", c)

vowcon(input("Enter string: "))
"""

#printing length  of a given word using fun
def length(w):
    count = 0
    for i in w:
        count += 1
    print("Length:", count)

word = input("Enter a word: ")
length(word)

