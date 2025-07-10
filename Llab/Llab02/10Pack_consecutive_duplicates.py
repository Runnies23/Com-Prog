
class Runner():
    def __init__(self):
        self.dict_data = []
        self.input_val = []
        self.get_input()
    
    def get_input(self):
        self.input_val = [i for i in input("InputList: ").replace("[",'').replace("'",'').replace("]",'').replace(' ','').split(',')]
        return 
    
    def print_output(self, text):
        print(text)

    def run(self):
        current = self.input_val[0]
        count = 0
        for i in self.input_val:
            if current == i:
                count += 1
            else: 
                try: 
                    current = int(current)
                except:
                    pass
                self.dict_data.append([current] * count)
                current = i
                count = 1

        
        try: 
            current = int(current)
        except:
            pass
        self.dict_data.append([current] * count)
        self.print_output(self.dict_data)
        return 


runner = Runner()
runner.run()
