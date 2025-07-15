# two pointer method 

class Runner():
    def __init__(self):
        self.input_val = None
        self.result = []
        self.get_input()

    def get_input(self):
        self.input_val = [int(i) for i in input('Enter list of number: ').split(' ')]

    def brute_force(self):
        n = len(self.input_val)
        for i in range(n):
            for j in range(i + 1, n):
                left = self.input_val[i]
                right = self.input_val[j]
                if abs(right - left) == 3:
                    self.result.append([left,right])
                    # break
        return 

    def run(self):
        self.brute_force()
        print(f"Output list: {self.result}")

runner = Runner()
runner.run()