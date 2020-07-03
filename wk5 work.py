
class Account:

    def __init__(self, balance, user):
        self.balance = balance
        self.user = user
        self.tax = 0
        if self.balance >= 1500 & self.balance < 4000:
             self.tax = 0.5
        elif balance > 4000:
            print("Hello ", user, "please provide a bank reference")

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print("5% withdrawl charge ")
            percentage = self.balance /100 * 5
            self.balance -= percentage
            

    def deposit(self, cash, amount):
        if cash:
            self.balance += amount
            process_deposit("cash", amount)
        elif cash == False:
            process_deposit("cheque", amount)
            
def process_deposit(method, amount):
        print("you added, £", amount, "to your account")
        print("payment method: ", method)

account1 = Account(200, "jim ravings")
account1.withdraw(110)
account1.deposit(True, 200)


    import math

    def circleArea(x):
        area = x ** 2 * math.pi
        print(area, " is your area")
        return area

    circleArea(4)

    def circleCircumfrance(y):
        circumfrance = y * math.pi
        print(circumfrance, " is the circumfrance")

    circleCircumfrance(12)

    def triangleArea(x, y):
        area = x * y / 2
        print(area, " is the area")

    triangleArea(12, 40)

    def volCylinder(x ,y):
        area = circleArea(x)
        cyVol = area * y
        print(cyVol, " is the volume of the cylinder")

    volCylinder(3, 4)

import random

def rps():
    options=["r", "p", "s"]
    r_index1 = random.randrange(0, len(options))
    r_index2 = random.randrange(0, len(options))

    d1 = options[r_index1]
    d2 = options[r_index2]
    
    print("user1 is ", d1)
    print("user2 is ", d2)
    
    if d1 == d2:
        print ("draw")
        
    elif d1 == "r" and d2 == "s":
        print("player 1 wins")
        
    elif d1 == "s" and d2 == "r":
        print("player 2 wins")
        
    elif d1 == "p" and d2 == "s":
        print("player 2 wins")
        
    elif d1 == "s" and d2 == "p":
        print("player 1 wins")
        
    elif d1 == "r" and d2 == "p":
        print("player 2 wins")
        
    elif d1 == "p" and d2 == "r":
        print("player 1 wins")

rps()

import math
    
class Pension:

    def __init__(self, salary, age, YoS, percentage):
        self.pension = 0
        self.salary  = salary
        self.age = age
        self.YoS = YoS
        self.percentage = percentage
    
    def pPension(self):
        p_y = self.salary * (self.percentage  / 100) * 12
        self.pension += p_y * self.YoS
        print("your pension amount is ", self.pension)

pension = Pension(2500, 65, 40, 12)
pension.pPension()
    
        
        
    
