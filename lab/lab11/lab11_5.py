from collections import defaultdict

class Runner():
    def __init__(self):
        self.save_data = defaultdict(lambda : {
            "subject-code" : None,
            "credits" : None,
            "grade" : None,
        })
        self.file_path = self.get_input()
        self.total_creditial = 0
        self.total_grade = 0

    def get_input(self):
        file_path = input("Enter grade file: ")
        return file_path
    
    def Turn_grade_to_nums(self, char):
        match char:
            case "A" : return 4.0
            case "B+" : return 3.5
            case "B" : return  3.0
            case "C+" : return 2.5
            case "C" : return 2.0
            case "D+" : return 1.5
            case "D" : return 1.0
            case _ : return 0.0
    
    def open_file(self, data_path:str):
        data = open(data_path).read().splitlines()
        return data
    
    def store_data(self, index,row):
        self.save_data[index]['subject-code'] = row[0]
        self.save_data[index]['credits'] = row[1]
        self.save_data[index]['grade'] = row[2]

    def cal_GPA(self):
        for key, value in self.save_data.items():
            temp_credits = int(value['credits'])
            temp_grade = self.Turn_grade_to_nums(value['grade'])
            print(f"subject: {value['subject-code']} credits: {temp_credits} grade: {value['grade']:<2} point: {temp_grade}")
            self.total_creditial += (temp_credits)
            self.total_grade += (temp_credits * temp_grade)
        return 

    def run(self):
        data = [i.split(",") for i in self.open_file(self.file_path) if i != ""]

        for index, item in enumerate(data):
            self.store_data(str(index), item)

        self.cal_GPA()
        print(f"Total credits = {self.total_creditial}\nGPA = {(self.total_grade / self.total_creditial):.2f}")


runner = Runner()
runner.run()

# grades1.txt