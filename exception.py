"""
try:
    a=int(input('a:'))
    b=int(input('b:'))
    print(a/b)
    
#except:
    #print("complete")
except ZeroDivisionError:
    print("you cant divide by 0")

except NameError:
    print("you enter a wrong name")
"""
"""
try:
    a=int(input('a:'))
    b=int(input('b:'))
    print(a+b)
    d={"a":10,"b":20,"c":30}
    print(d[x])
    
except TypeError:
    print("you cannot + int and str")
    
except IndexError:
    print("Index out of range")
    
except ZeroDivisionError:
    print("not divisible by 0")
    
except NameError:
    print("key not found")
    
finally:
    print("completed")
    """
"""
try:
    d={1:"a"}
    print(d[a])
except Exception as triveni:
    print(triveni)
finally:
    print("completed")
    """
#value error
"""
pin=1234
a=int(input("a:"))
if pin!=a:
    raise ValueError("only integer values")
else:
    print("success")
    """
#raise errors
    
try:
    age=int(input('age:'))
    if age<18:
        raise ValueError("
        