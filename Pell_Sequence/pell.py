# Pell Numbers


class Pell:
    def __init__(self):
        self.limiter = 1000
        self.numbers = [0, 1]
        self.path = r'./Pell_Sequence/results.txt'
        
    def void(self):
        with open(self.path, "w+") as file:
            for i in range(self.limiter):
                self.numbers.append(2 * self.numbers[i+1] + self.numbers[i])
            file.writelines(f'{self.numbers}\n')


Start = Pell()
Start.void()
        