# Score Ranking



class Runner():
    def __init__(self):
        self.data = []
        self.get_input()

    def sort_array(self):
        self.data = sorted(self.data)

    def get_input(self):
        status  = True  
        while status:
            input_val = input('Enter student score (or just ENTER to finish): ')
            if input_val == "":
                status = False
                continue
            else: 
                self.data.append(int(input_val))

    def print_output(self):
        for index, item in enumerate(self.data[::-1]):
            print(f"Rank #{index+1}: {item}")
        return 


    def run(self):
        if len(self.data) == 0:
            return 
        else: 
            self.sort_array()
            self.print_output()
            return


runner = Runner()
runner.run()