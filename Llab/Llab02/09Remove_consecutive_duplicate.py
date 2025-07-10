
class Runner():
    def __init__(self):
        self.data = None
        self.get_input()
        self.seen = set()
        self.result = []

    def get_input(self):
        self.data = [i for i in input("InputList: ").replace(']','').replace('[','').replace(' ','').replace("'",'').replace("'",'').split(',')]

    def run(self):
        pass_val = None
        for i in self.data:
            if i != pass_val:
                pass_val = i 
                try:
                    self.result.append(int(i))
                except:
                    self.result.append(i)


        print(self.result)


runner = Runner()
runner.run()