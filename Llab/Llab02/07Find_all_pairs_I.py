# two pointer method 

class Runner():
    def __init__(self):
        self.input_val = None
        self.result = []
        self.seen = set()
        self.get_input()

    def get_input(self):
        self.input_val = [int(i) for i in input('Enter list of number: ').split(' ')]

    def brute_force(self):
        for i in range(len(self.input_val)):
            for j in range(i + 1, len(self.input_val)):
                left = self.input_val[i]
                right = self.input_val[j]
                if left != right and left not in self.seen and right not in self.seen:
                    if (left >= 0 and right >= 0) or (left <= 0 and right <= 0):
                        if (abs(right) - abs(left)) == 3:
                            self.result.append([left,right])

                            self.seen.add(left)
                            self.seen.add(right)
                            break

                    else:   
                        if abs(right - left) == 3:
                            self.result.append([left,right])

                            self.seen.add(left)
                            self.seen.add(right)
                            break

        return 

    def run(self):
        self.brute_force()
        print(f"Output list: {self.result}")

runner = Runner()
runner.run()