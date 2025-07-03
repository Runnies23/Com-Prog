class Score_Grading():
    def __init__(self):
        pass
        self.data = []
        self.status = True
        self.mean = None
        self.std = None

    def Gradding(self,score):
        if score > 0 and score <= 100:
            if score >= self.mean + (1.5 * self.std):
                return "A"
            elif score >= self.mean + (1.0 * self.std):
                return "B+"
            elif score >= self.mean + (0.5 * self.std):
                return "B"
            elif score >= self.mean:
                return "C+"
            elif score >= self.mean - (0.5 * self.std):
                return "C"
            elif score >= self.mean - (1.0 * self.std):
                return "D+"
            elif score >= self.mean - (1.5 * self.std):
                return "D"
            else:
                return "F"
        else:
            return "Out of range(0,100)"

    def calculate_mean_std(self):
        self.mean = sum(self.data)/len(self.data)
        process_data = [(i-self.mean)**2 for i in self.data]
        self.std = (sum(process_data) / (len(process_data)  - 1)) ** 0.5

    def get_input(self):
        while self.status:
            input_value = input("Enter score (or ENTER to finish): ")
            if input_value == "":
                self.status = False
            else:
                self.data.append(int(input_value))

    def print_output(self):
        print(f"""Average score is {self.mean:.2f}\nStandard deviation is {self.std:.2f}""")    
        for index, item in enumerate(self.data):
            print(f"Student #{index+1} score: {item:d} grade: {self.Gradding(item)}")

    def Do_smth(self):
        self.get_input()
        self.calculate_mean_std()
        if self.mean is None or self.std is None:
            return
        self.print_output()

grader = Score_Grading()
grader.Do_smth()