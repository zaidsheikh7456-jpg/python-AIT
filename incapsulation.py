class Student:
    def __init__(self):
        self.__grade = None

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade")

    def is_passed(self):
        if self.__grade >= 50:
            return "Passed"
        else:
            return "Failed"

s = Student()
s.set_grade(120)
s.set_grade(85)
print("Grade:",s.get_grade())
print("Status:",s.is_passed())
 
 
class Product:
    def __init__(self):
        self.__price = 0

    def get_price(self):
        return self.__price

    def set_price(self, amount):
        if amount > 0:
            self.__price = amount
        else:
            print("Invalid price")

    def apply_discount(self, percent):
        if 0 < percent < 100:
            self.__price -= self.__price * percent / 100

p = Product()
p.set_price(-50)
p.set_price(1000)
print("Price after setting:", p.get_price())
p.apply_discount(20)
print("Price after discount:", p.get_price())



class Employee:
    def __init__(self):
        self.__salary = 0

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount >= 0:
            self.__salary = amount
        else:
            print("Invalid salary")

    def increase_salary(self, percent):
        self.__salary += self.__salary * percent / 100

e = Employee()
e.set_salary(-1000)
e.set_salary(5000)
print("Salary after setting:", e.get_salary())
e.increase_salary(10)
print("Salary after increment:", e.get_salary())



class Car:
    def __init__(self):
        self.__speed = 0

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        if value >= 0:
            self.__speed = value
        else:
            print("Invalid speed")

    def accelerate(self, amount):
        self.__speed += amount

    def brake(self, amount):
        self.__speed = max(0, self.__speed - amount)

c = Car()
c.set_speed(-20)
c.set_speed(50)
print("Speed after setting:", c.get_speed())
c.accelerate(30)
print("Speed after acceleration:", c.get_speed())
c.brake(60)
print("Speed after braking:", c.get_speed())
print("Final speed:", c.get_speed())



class BankAccount:
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Invalid balance amount")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

b = BankAccount()
b.set_balance(-200)
b.deposit(500)
print("Balance after deposit:", b.get_balance())
b.withdraw(300)
print("Balance after withdrawal:", b.get_balance())
print("Final balance:", b.get_balance())
