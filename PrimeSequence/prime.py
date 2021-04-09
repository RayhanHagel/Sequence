from math import ceil


# Algorithm to find Prime Numbers
class Prime:
    def __init__(self):
        self.path = r'./PrimeSequence/results.txt'
        self.limit = 10000 # Change this to get certain range result
        self.list = []
        self.num = 1
    
    def void(self):
        if self.num < 100:
            for i in range(2, self.num):
                if self.num % 2 == 0:
                    break
                if self.num % i == 0:
                    break
            else:
                self.list.append(self.num)
        elif self.num > 100:
            for i in range(1, ceil(self.num/4)):
                if self.num % 2 == 0:
                    break
                if self.num % (i*2+1) == 0:
                    break
            else:
                self.list.append(self.num)  
        
    def loop(self):
        file = open(self.path, "w+")
        for i in range(2, self.limit):
            self.num = i
            self.void()
        file.writelines(f'{self.list}\n')
        # print(self.list) - Optional
                    
                    
Start = Prime()
Start.loop()
