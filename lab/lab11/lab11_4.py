data = open("scores1.txt").read().splitlines()

class Process():
    def __init__(self):
        self.data = None

    def open_file(self, data_path):
        data = open(data_path).read().splitlines()
        return data

    def get_input(self):
        data_path = input("Enter score file: ")
        self.data = self.open_file(data_path)

    def print_output(self):
        for index, item in enumerate(self.data):
            print(f"Student #{index+1} score: {item}")
        print(f"Average score is {(sum(self.data)/len(self.data)):.2f}")
        print(f"Minimum score is {min(self.data)}")
        print(f"Maximum score is {max(self.data)}")

    def run(self):
        self.get_input()
        self.data = [int(i) for i in self.data if i != ""]
        self.print_output()

    

runner = Process()
runner.run()
