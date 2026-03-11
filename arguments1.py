"""def Details(name,age):
    print(f"{name},name")
    print(f"{age},age")
Details(age=12,name="triv")"""

#positional arguments
"""
def student(name, age, address, phno, marks):
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)
    print("Phone Number:", phno)
    print("Marks:", marks)
student("Triveni", 21, "guntur", 00000000000, 85)"""

#keyword argguments
"""
def student(name, age, address, phno, marks):
    print("Name:", name)
    print("Age:", age)
    print("Address:", address)
    print("Phone Number:", phno)
    print("Marks:", marks)

student(age=21, name="Triveni", marks=85, phno=01010101010, address="guntur")"""
#default arguments
"""
def Details(name,age,place="hyd"):
    
    print(f"{name},name")
    print(f"{age},age")
    print(f"{place},place")
Details("triveni",21,"vij")
print()
Details("avani",25)
"""
"""
def Add(*args):
    print(*args)#if we doesnot need the data in tuple then we use *args
    print(sum(args))
Add(10,20)
Add(1,2,3)
Add(1,2,3,4)
"""
def user(name, marks, *hobbies, place="Unknown", **other):
    print("Name:",name)              # Positional
    print("Marks:",marks)            # Keyword
    
    print("Place:",gnt)            # Default
    
    print("Hobbies:")
    for i in hobbies:             # *args
        print(i)
    
    print("other:")
    for key, value in other.items():  # **kwargs
        print(key, ":", value)

user(
    "Triveni",                
    marks=95,                  
    "singing", "kdrama",      
    place="guntur",       
    age=20, course="B.Tech")

    