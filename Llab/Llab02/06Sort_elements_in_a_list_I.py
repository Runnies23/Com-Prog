
class Runner():
    def __init__(self):
        self.input_val = []
        self.lst_of_tuple = []
        self.data_dict = {}
        self.get_input()
        pass

    def get_input(self):
        self.input_val = [int(i) for i in input("Enter list of tuple: ").split()]

    def print_output(self, output):
        print(f"Input list: {self.lst_of_tuple}")
        print(f"Output list: {output}")

    def run(self):

        for i in self.input_val:
            temp = []
            for j in str(i):
                temp.append(int(j))
            self.lst_of_tuple.append(tuple(temp))

            self.data_dict[j[-1]] = tuple(temp)

        result = []
        for i in sorted(runner.data_dict.keys()):
            result.append(tuple(runner.data_dict[i]))

        self.print_output(result)

        return 

runner = Runner()
runner.run()