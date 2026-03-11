#Searching and Checking Methods
a="codegnan"
"""
print(a.find("n"))#find
print(a.rfind("N"))#rfind
print(a.index("o"))#index

roll="abc123"
roll1="234"
print(roll.startswith("abc"))#startswith
print(roll1.startswith("abc"))

mail="tri@gmail.com"
print(mail.endswith("gmail.com"))#endswith
print(mail.count("c"))#count
"""

#Modification methods
#strip()-whenever there is space the strip removes it
"""
x="####nothing is impossible###"
print(x.strip('#'))
#lstrip()-only left side spaces or unwanted
print(x.lstrip('#'))
#rstrip()-only right side spaces or unwanted
print(x.rstrip('#'))
#replace()-it used to replce the words
y="nothing is possible"
print(y.replace("possible","impossible"))


#splitting and joining methods
#split-seperate chestam when there is space[string to list]
z="nothing is possible"
print(z.split(" "))
#join -list to string
print("".join(z))
"""

#Advanced formatting
x="next-gen"
print(x.rjust(10,"*"))
print(x.ljust(10,"*"))
print(x.center(15,"*"))
print(x.zfill(5))
print(x.paritition("-"))


