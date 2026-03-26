#single inheritace-child class can only take properties of parent but not from parent to child

"""class Father:
    def F1(Self):
        print("this is father class")
class Triveni(Father):
    def C1(self):
         print("this is child class")
child1=Triveni()
child1.F1()"""

#multilevel-child-father,grandfather,father-grandfather
"""
class Grand_Father:
    def G1(self):
        print("this is grandparent class")
class Father(Grand_Father):
    def F1(self):
        print("this  is father class")
class Child(Father):
    def C1(self):
        print("this is child class")
#father can access from grandparent
f=Father()
f.G1()
#child van access from both father,grandparent
c=Child()
c.F1()
c.G1()
"""

#multiple inheritance-child->mother,father
"""class Father:
    def F1(self):
        print("this is father class")
class Mother:
    def M1(self):
        print("this is mother class")
class Child(Father,Mother):
    def C1(self):
        print("this is child class")
c=Child()
c.F1()
c.M1()
"""
"""
class Employee:
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Role:",self.role)
class Manager(Employee):
   def increment(self):
       self.salary=self.salary+100
m1=Manager("triveni",45000,"manager")
m1.increment()
m1.display()
"""
"""
class Restaurant:
    def order_food(self):
        print("Food ordered from restaurant")

class Delivery:
    def delivery_process(self):
        print("Food is out for delivery")

class Zomato(Restaurant, Delivery):
    def zomato_service(self):
        print("Welcome to Zomato service")

z = Zomato()
z.zomato_service()
z.order_food()
z.delivery_process()"""
"""
class parent:
    def p1(self):
        print("parent")
class brother(parent):
    def b1(self):
        print("brother")
class sister(parent):
    def s1(self):
        print("sister")
C1=sister()
C2=brother()
C2.b1()
C2.p1()
C1.s1()
C1.p1()"""
"""
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def type(self, fuel_type):
        print(f"{self.brand} car type: {fuel_type}")


class Bike(Vehicle):
    def mileage(self, mileage):
        print(f"{self.brand} bike mileage: {mileage} kmpl")


car_brand = input("Enter car brand: ")
car_type = input("Enter car type (Petrol/Diesel/EV): ")

bike_brand = input("Enter bike brand: ")
bike_mileage = input("Enter bike mileage: ")

c = Car(car_brand)
b = Bike(bike_brand)
c.type(car_type)
b.mileage(bike_mileage)"""
"""
class BankAccount:
    def __init__(self):
        self.balance = 1200.0  # Shared property

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}")

    def display_total(self):
        print(f"Total Balance: ${self.balance}")

class Savings(BankAccount):
    def savings_info(self):
        print("This is a Savings Account.")


class Current(BankAccount):
    def current_info(self):
        print("This is a Current Account.")

tri = Savings()
tri.deposit(500)     
tri.display_total()   
veni = Current()
veni.deposit(1000)     
veni.display_total()
"""
"""
class Father:
    def C2(self):
        print("this is father class")
class Sathwik(Father):
    def C1(self):
        print("this is child1 class sat")
class Krishna_sathwik(sathwik):
    def C2(self):
        print("this is child2 class krishna_satwik")
obj=krishna_sathwik()
obj.c2()"""
"""
class bts:
    def jk(self):
        print("euphoria")
class maknae(bts):
    def v(self):
        print("serendipity")
class Cute(maknae):
    def jimin(self):
        print("promise")
obj = Cute()
obj.jimin()"""

class Vehicle:
    def v1(self):
        print("this is Vehicle class")
class Bike(Vehicle):
    def v1(self):
        print("this is Bike class")
class Car(Bike):
    def v1(self):
        print("this is Car class")
obj=Car()
obj.v1()