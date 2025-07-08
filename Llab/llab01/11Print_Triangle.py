
class Runner():
    def __init__(self):
        self.nums = None
        self.text = "x"
        self.get_input()

    def get_input(self):
        status = True
        while status:
            nums_input = int(input("Input number: "))
            if nums_input % 2 == 0:
                print("Please input odd number")
            else:
                self.nums = nums_input
                status = False

    def run(self):
        for i in range(self.nums * 2):
            print(self.text * (self.nums - abs(self.nums - i)),end=" ")
            print()
        pass


runner = Runner()
runner.run()


# x
# xx
# xxx
# xxxx
# xxxxx
# xxxxxx
# xxxxxxx
# xxxxxx
# xxxxx
# xxxx
# xxx
# xx
# x
