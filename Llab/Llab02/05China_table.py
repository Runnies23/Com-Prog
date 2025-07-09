
def plus(total,value):
    return total + value

def minus(total,value):
    return total - value

class Runner():
    def __init__(self):
        self.data = []
        self.operation = []
        self.total = 0
        self.get_input()

    def get_input(self):
        time = int(input("How many food you have : "))
        for _ in range(time):
            val = input().split()
            self.data.append(int(val[0]))
            self.operation.append(int(val[1]))

    def run(self):
        if len(self.data) == 0 and len(self.data) != len(self.operation):
            return 
        else: 
            for index, i in enumerate(self.operation):
                if i > 0:
                    self.total = plus(self.total, self.data[index])
                else: 
                    self.total = minus(self.total, self.data[index])

        print(self.total)


runner = Runner()
runner.run()