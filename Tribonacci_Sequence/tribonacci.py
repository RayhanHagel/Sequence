# Tribonacci Numbers Algorithm


class Tribonacci:
    def __init__(self):
        self.list = ["0", "0", "1"]
        self.limit = 1000
        self.path = r'./Tribonacci_Sequence/results.txt'
    
    def setup(self):
        for i in range(self.limit):
            self.list.append(str(int(self.list[i]) + int(self.list[i+1]) + int(self.list[i+2])))
        with open(self.path, 'w+') as file:
            file.writelines(f'{self.list}')

Start = Tribonacci()
Start.setup()
