"""
f=open("file.txt",mode="r+")
f.seek(0)
f.write("\n***************")
f.write("\n hide in the moonlight ")
f.write("\n euphoria")

print("done")
f.close()

import os
print(os.getcwd())
"""
import os
def Write():
    with open("basic.csv",mode="w") as file:
        if os.path.getsize("basic.csv")==0:
            file.write("name,age,marks\n")
            print("done")
            
def Read():
    with open("basic.csv","r") as file:
        data=file.readlines()
        for i in data:
            print(i)
            
def Update():
    if os.path.exists("basic.csv"):
        with open("basic.csv","r") as file:
            name=input("name:")
            data=file.readlines()
            for i in data:
                details=i.split(",")
                if details[0]==name: 
                    print("already exists")
                    break
                
            else:
                with open("basic.csv","a") as file:
                    age=int(input("age:"))
                    marks=float(input("marks:"))
                    file.write(f"{name},{age},{marks}\n")
                print("succefully updated")
    else:
        print("path not exists")
        
def Delete():
    if os.path.exists("basic.csv"):
        name=input("enter del name:")
        with open("basic.csv","r") as file:
            data=file.readlines()    
        Flage=False
        l=[]
        with open ("basic.csv","w") as file:
            for i in data:
                details=i.split(",")
                if details[0]!=name:
                    l.append(i)
                    print(l)
                else:
                    Flage=True
            with open ("basic.csv","w") as file:
                file.writelines(l)
               
            if Flage==True:
                print("deleted succefully")
            else:
                print("element not found")
                    
        
    


while True:
    print("1.write\n2.read\n3.Update\n4.delet")
    n=int(input("enter proper input"))
    if n==1:
        Write()
    elif n==2:
        Read()
    elif n==3:
        Update()
    elif n==4:
        Delete()