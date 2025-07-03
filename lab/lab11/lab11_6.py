
class Runner():
    def __init__(self):
        self.file_path = None
        self.Old_age = None
        self.save_data = set()
        pass

    def get_input(self):
        self.file_path = input("Enter age file: ")
        data = [i.split(",") for i in open(self.file_path).read().splitlines() if i != '']
        return data
    
    def run(self):
        data = self.get_input()
        self.save_data = set([i[1] for i in data])

        max_age = max(self.save_data)

        print(f"Oldest person(s) with the age of {max_age}:")
        for name, age in data:
            if age == max_age:
                print(f"- {name}")

runner = Runner()
runner.run()