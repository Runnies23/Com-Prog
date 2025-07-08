

class Runner():
    def __init__(self):
        pass

    def run(self):
        Manchester = input("What's the result of Manchester city's match? ")
        Liverpool = input("What's the result of Liverpool's match? ")


        if Manchester == Liverpool == 'won':
            Manchester_point = input("What is the margin that Manchester city won by? ")
            Liverpool_point = input("What is the margin that Liverpool won by? ")
            if Manchester_point != Liverpool_point:
                print("Manchester city is the champion of Premier League." if Manchester_point > Liverpool_point \
                else "Liverpool is the champion of Premier League.")

            else:
                win_team = input("Which team won the play-off match?(Manchester city/Liverpool) ")
                print(f"{win_team} is the champion of Premier League.")
        else:
            print("Manchester city is the champion of Premier League." if Manchester == 'won' \
                else "Liverpool is the champion of Premier League.")

runner = Runner()
runner.run()
