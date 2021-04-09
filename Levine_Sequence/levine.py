# This code solves the Levine Sequence


class LevineSequence:
    def __init__(self):
        self.start = ["2"]
        self.split = ["2"]
        self.result = ""
        self.len = 0
        self.path = r'./Levine_Sequence/results.txt'

    def void(self):
        self.start = self.split
        self.split = []
        self.len = len(self.start)

    def counter(self):
        for x in range(self.len):
            for y in range(int(self.start[self.len-x-1])):
                self.split.append(int(x+1))
        self.result = str(sum(self.split)) + "\n"

    def write(self):
        file = open(self.path, "w+")
        file.writelines(self.result)
        file.close()

    def loop(self):
        while True:
            self.void()
            self.counter()
            self.write()


Start = LevineSequence()
Start.loop()
