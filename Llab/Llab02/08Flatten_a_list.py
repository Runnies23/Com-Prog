
class Runner():
    def __init__(self):
        self.input_val = None
        self.result = []
        self.get_input()

    def get_input(self):
        self.input_val = input('Original list: ').replace('[','').replace(']','').replace('"',"").replace("'",'')

    # def method_1_array(self):
    #     for i in self.input_val:
    #         if type(i) == list:
    #             for j in i:
    #                 self.result.append(j)

    #         else: 
    #             self.result.append(i)

    def run(self): #text 
        result = []
        for i in runner.input_val.split(','):
            try: 
                result.append(int(i))
            except:
                result.append(i)
        
        print(f"Flatten list: {result}")

        pass


runner = Runner()
runner.run()