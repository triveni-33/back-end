"""
class Showroom:
    def __init__(self, name, model, rate, color, mileage):
        self.name = name
        self.model = model
        self.rate = rate
        self.color = color
        self.mileage = mileage
    
Information = Showroom("volkswagen", "lamborghini", "4 cr", "burgundy", "325 kmph")
print("Company:", Information.name)
print("Model:", Information.model)
print("rate:", Information.rate)
print("color:", Information.color)
print("Mileage:", Information.mileage)
"""
"""
class Base:
    def __init__(self,name,age):
        self.name=name
        self.age=age
output=Base("Triveni","21")
print("Name:",output.name)
print("Age:",output.age)
"""
"""
#initialisation attribute
class Base:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def method(self):
        print(self.name,self.age)
    
output=Base("Triveni","21")
output.method()
"""
class ATM:
    def __init__(self):
        self.__pin = 1438        
        self.__balance = 1000    

    
    def verify_pin(self):
        attempts = 3
        while attempts > 0:
            pin = int(input("Enter PIN: "))
            if pin == self.__pin:
                return True
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong PIN! Attempts left: {attempts}")
                else:
                    print("Card Blocked!")
        return False

    
    def deposit(self, amount):
        if amount > 0:
            print("Previous Balance:", self.__balance)
            self.__balance += amount
            print("Deposited Amount:", amount)
            print("Updated Balance:", self.__balance)
        else:
            print("Invalid amount (must be > 0)")

    
    def balance(self):
        print("Total Balance:", self.__balance)


atm = ATM()

if atm.verify_pin():
    amount = int(input("Enter amount to deposit: "))
    atm.deposit(amount)
    atm.balance()
