# two pointer method 


class Runner():
    def __init__(self):
        self.input_val = None
        self.result = []
        self.get_input()

    def get_input(self):
        self.input_val = input('Enter list of number: '.split())

    def brute_force(self):
        for i in range(len(self.input_val)):
            for j in range(i, len(self.input_val)):
                if (i + j) % 3 == 0:
                    self.result.append[i,j]
        return 

    def run(self):

        self.brute_force()

        pass


runner = Runner()
runner.run()