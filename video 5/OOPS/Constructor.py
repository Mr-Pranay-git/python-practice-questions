class Car:
    def __init__(self, BT, ET, Tyres):
        self.BT = BT
        self.Tyres = Tyres
        self.ET = ET
    
    def hello(self):
        print(f"your details are {self.BT}, {self.ET}, {self.Tyres}")

Lambo =  Car("Covered", 4,"2 cycles")

Lambo.hello()