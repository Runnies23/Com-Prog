class BankNote:
    def __init__(self, value = 20):
        self.value = value
        self.bank = [1000,500,100,50,20]

    def __str__(self):
        return f'{self.value} Baht Banknote'
    

    def run(self):
        for bank in self.bank:
            if self.value >= bank:
                print(f"You get {self.value // bank} of {bank} Baht Banknote")
                
                self.value %= bank
        return self.value
    
class Coin:
    def __init__(self, value = 1):
        self.value = value
        self.Coin = [10,5,2,1]

    def __str__(self):
        return f'{self.value} Baht Coin'
    
    def run(self):
        for coin in self.Coin:
            if self.value >= coin:
                print(f"You get {self.value // coin} of {coin} Baht Coin")
                self.value %= coin
            if coin == 1 and self.value != 0:
                print(f"You get {self.value // coin} of {coin} Baht Coin")


amount = int(input("Input amount : "))
Bank = BankNote(amount)
remain = Bank.run()
coin = Coin(remain)
coin.run()