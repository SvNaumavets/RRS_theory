print('ex. 1')
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

rect = Rectangle(2,4)
print(f"a = rect.area() = {rect.area()}")
print(f"p = rect.perimeter() = {rect.perimeter()}")

######################################################################################

print("ex. 2")
class Car:

    def __init__(self, marke, max_speed):
        self.marke = marke
        self.max_speed = max_speed
        self.speed = 0

    def display_speed(self):
        print(self.speed)

    def accelerate(self):
        if self.speed > self.max_speed - 10:
           self.speed = self.max_speed
        else:
            self.speed += 10
        return self.speed

    def brake(self):
        if self.speed < 10:
            self.speed = 0
        else:
            self.speed -= 10
        return self.speed

my_toyota = Car("Toyota", 180)
for _ in range(20):
    my_toyota.accelerate()
my_toyota.display_speed()
for _ in range(22):
    my_toyota.brake()
my_toyota.display_speed()

#######################################################################################

print("ex. 3")
class BankAccount:

    def __init__(self, _name, _balance):
        self._name = _name
        self._balance = _balance

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def withdraw(self, amount):
        if self.get_balance() < amount:
            print("Недостаточно средств!")
        else:
            self._balance -= amount
            return self._balance

account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance())
account.withdraw(2000)

###########################################################################################

print("ex. 4")
class OverdraftAccount(BankAccount):

    def withdraw(self, amount):
        self._balance -= amount
        return self._balance

jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
jack_account.withdraw(100)
jack_account.withdraw(100)
print(jack_account.get_balance())




