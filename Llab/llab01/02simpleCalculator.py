
class Runner():
    def __init__(self):
        self.x = None
        self.y = None

    def calculator(self, a,b, ops):
        match ops:
            case "+" : result = a + b
            case "-" : result = a - b
            case "*" : result = a * b
            case "/" : result = f"{(a / b):.2f}"
            case "%" : result = a % b
            case _ : result = "Unknown Operator"
        return result

    def run(self):
        self.x = int(input("x: "))
        self.operation = input("Operator: ")
        self.y = int(input("y: "))
        if self.x is not None and self.y is not None:
            print(self.calculator(self.x, self.y,self.operation))


runner = Runner()
runner.run()