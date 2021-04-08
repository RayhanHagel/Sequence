import time

# Initiates the first pattern
class Kolakoski:
    def __init__(self):
        self.sequence = "12"
        self.split = []
        self.num1, self.num2 = "1", "2"
        self.path = r'./KolakoskiSequence/results.txt'
        
    def decoder(self):
        self.num1, self.num2 = "1", "2"
        self.split = list(self.sequence)
        self.sequence = ""
        for x in self.split:
            self.sequence = self.sequence + (str(self.num1) * int(x))
            self.num1, self.num2 = self.num2, self.num1
        # Optional - print(self.sequence)

    def loop(self):
        file = open(self.path, "a")    
        while True:
            self.decoder()
            file.writelines(f'{self.sequence}\n')

Start = Kolakoski()
Start.loop()
        