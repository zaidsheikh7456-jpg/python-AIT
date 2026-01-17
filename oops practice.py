
class Car:
    def __init__(self, brand, color, speed):
        self.brand = brand      # brand attribute
        self.color = color      # color attribute
        self.speed = speed      # speed attribute

    
    def display_info(self):
        print("Brand:", self.brand)
        print("Color:", self.color)
        print("Speed:", self.speed, "km/h")


car1 = Car("Toyota", "Red", 180)
car2 = Car("Honda", "Blue", 160)


car1.display_info()
print("----")
car2.display_info()