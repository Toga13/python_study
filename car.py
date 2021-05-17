class Car:
    def __init__(self, color):
        self.color = color 
        self.msg = "これは車クラスです"

    def show_color(self):
        print (self.color)

    def accele(self):
        print ("アクセルを踏みました．")

    def run(self, speed):
        print (f"{speed}km/hで走る．")

    def show_msg(self):
        print (self.msg)

car = Car("black")
car.run(100)
car.show_color()
car.show_msg()