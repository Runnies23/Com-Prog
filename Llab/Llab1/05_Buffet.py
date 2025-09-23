
class Runner():
    def __init__(self):
        self.price = {
            "Korean" : 1_500,
            "Japanese" : 1_000
        }

    def run(self):
        choice = input('Enter your buffet choice: ')
        if choice in ['Korean','Japanese']:
            wednes_day = input("Is today Wednesday (yes/no)? ")
            print(f"Your payment is {(self.price[choice] * 0.85 if wednes_day == 'yes' else self.price[choice]):.2f} Baht.")

        else:
            print(f"Sorry, there is no {choice} buffet.")
        pass


runner = Runner()
runner.run()