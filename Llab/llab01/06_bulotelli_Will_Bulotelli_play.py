
class Runner():
    def __init__(self):
        pass

    def run(self):
        if input("Is Bulotelli injured?(y/n) ") == 'n':
            if input('Is Bulotelli late for the training?(y/n) ') == "y":
                if input('Did Bulotelli perform well in training?(y/n) ') == 'y':
                    print('Substitute')
                else:
                    print('Not selected')
            else:
                print('Starter')

        else:
            print("Not available")
        pass


runner = Runner()
runner.run()