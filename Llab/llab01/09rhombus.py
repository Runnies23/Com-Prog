
class Runner():
    def __init__(self):
        self.nums = None
        pass

    def run(self):
        self.nums = int(input("input: "))
        for i in range(1, self.nums+1):
            print(" " * (self.nums - i - 1),end="")
            print("#" * (i * 2 - 1 ))

        pass


runner = Runner()
runner.run()