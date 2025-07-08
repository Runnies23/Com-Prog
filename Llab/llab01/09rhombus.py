
class Runner():
    def __init__(self):
        self.nums = None
        pass

    def run(self):
        self.nums = int(input("input: "))
        for i in range(1, self.nums+1):
            print(" " * (abs(self.nums - ((i * 2)-1))//2),end="")
            print("#" * (self.nums - (abs(self.nums - ((i * 2)- 1)))))

        pass


runner = Runner()
runner.run()