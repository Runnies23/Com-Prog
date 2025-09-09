'''
    turtle_BJ.py (aka. version 1.1) brewed by KunToto@MikeLabDotNet [August 2024]
'''
import random, time
# import turtle

class Card():
    ''' Card(): create a card object. To create a deck, try \Card.test_Card()\! '''
    symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
    def get_name(self):
        return self.name
    def get_suit(self):
        return self.suit
    def __repr__(self):
        return f"{self.name}{Card.symbols[self.suit]}"
    def test_Card():
        Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
        Suits = ['D','C','H','S']
        deck = [Card(str(n), s) for s in Suits for n in Names]
        random.shuffle(deck)
        res = [str(card) for card in deck]
        return ' '.join(res)
    #---------------------------------------------------------------------
    def render(self, x, y, color='blue', RENDER=False):
        ''' วาดไพ่ด้วยเต่า '''
        if not RENDER:
            return None
        # Draw border
        pen.penup()
        pen.color(color)
        pen.goto(x+50, y+75)
        xy = ((x+50, y+75), (x+50, y-75), (x-50, y-75), (x-50, y+75))
        pen.begin_fill()
        pen.pendown()
        for pos in xy:
            pen.goto(pos)
        pen.end_fill()
        pen.penup()
        # Draw card info
        if self.name not in ['','O']:
            # Draw suit in the middle
            pen.color('white')
            pen.goto(x-18, y-30)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
            # Draw top left
            pen.goto(x-40, y+45)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x-40, y+25)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
            # Draw bottom right
            pen.goto(x+30, y-60)
            pen.write(self.name, False, font=("Courier New", 18, "normal"))
            pen.goto(x+30, y-80)
            pen.write(self.symbols[self.suit], False, font=("Courier New", 18, "normal"))
        pen.penup()
    #---------------------------------------------------------------------

class Deck:
    ''' Deck(): สร้างสำรับไพ่ '''
    Names = ['A',2,3,4,5,6,7,8,9,'T','J','Q','K']
    Suits = ['D','C','H','S']
    def __init__(self):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
    def shuffle(self):
        random.shuffle(self.cards)
    def get_card(self):
        return self.cards.pop()
    def set_cards(self, cards):
        self.cards = cards
    def reset(self, n=1):
        Names, Suits = Deck.Names, Deck.Suits
        self.cards = [Card(str(n), s) for s in Suits for n in Names]
        for i in range(n):
            self.shuffle()
    def __repr__(self):
        res = [str(x) for x in self.cards]
        return ' '.join(res)

def preamble(RENDER=False):
    ''' จัดการ environment ในการวาดเต่า '''
    if not RENDER:
        return None
    #--------------------------------------------------------------------------------------
    global wn, pen
    wn, pen = turtle.Screen(), turtle.Turtle()
    wn.bgcolor('black')
    wn.setup(800, 600)
    wn.title('Deck of Cards Simulator by @TokyoEdtech, rebrewed by KunTotoNaMikeLabDotNet')
    pen.speed(0)
    pen.hideturtle()
    #--------------------------------------------------------------------------------------

def test_turtle_deck(RENDER=False):
    ''' ไว้ตรวจสอบเต่าวาดไพ่ ฟังชัน Card.render() '''
    preamble(RENDER)
    # create a deck f card
    deck = Deck()
    # shuffle deck
    deck.reset()
    print(deck)
    # render n cards (back) in a row
    nbOfCards = 5
    start_x = -250
    for x in range(nbOfCards):
        card = Card('', '')
        card.render(start_x + x*125, 175, 'orange', RENDER=True)
    time.sleep(1)
    # re-render n cards in a row
    start_x = -250
    for x in range(nbOfCards):
        card = deck.get_card()
        card.render(start_x + x*125, 175, RENDER=True)
    print('Done..')

def createVirtualDeck(s='K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'):
    dd = s.split()
    res = []
    suit = {'♦':'D','♣':'C','♥':'H','♠':'S'}
    for d in dd:
        card = Card(d[0], suit[d[1]])
        res.append(card)
    deck = Deck()
    deck.set_cards(res)
    return deck


#==============================================Submist this block (start) ==============================================

class myCard:
    ''' myCard(): ลิสเก็บไพ่ที่ผู้เล่นถืออยู่ '''

    def __init__(self, name:str):
        self.name = name
        self.card = []
        self.card_name = []
        self.score = 0
        self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
        self.score_map = {
            'A' : 11,
            '2' : 2,
            '3' : 3,
            '4' : 4,
            '5' : 5,
            '6' : 6,
            '7' : 7,
            '8' : 8,
            '9' : 9,
            'T' : 10,
            'J' : 10,
            'Q' : 10,
            'K' : 10}

    def get_card(self, card):
        self.card.append(card)
        self.card_name.append(card.name)
        if card.name == "A" and self.score + 11 > 21:
            temp_scrore = 1
            self.score += temp_scrore
            return
        
        if self.score + self.score_map[card.name] > 21 and "A" in self.card_name:
            self.score -= 10
            self.card_name.remove("A")

        self.score += self.score_map[card.name]


    def print_hidden(self):
        print(f"{self.name:>9}: {" ".join(["O" + self.symbols[self.card[0].get_suit()], str(self.card[1])]):<16}-> {self.score_map[self.card[1].name]}")
        
    def print_normal(self):
        print(f"{self.name:>9}: {" ".join([str(i) for i in self.card]) :<16}-> {self.score}")

    def checkEndGame(self):
        if self.score == 21 or len(self.card) == 5 or self.score > 21:
            return True

    def get_more_card(self, player_score, player_card):
        if self.score <= 16 or (self.score < player_score and player_score <= 21) or (player_card == 5 and player_score <= 21):
            return True
        
    def check_blackjack(self):
        if (self.score == 21 and len(self.card) == 2):
            return True
        if (self.score <= 21 and len(self.card) == 5):
            return True
        else: 
            False


def print_result(com, player, com_score, player_score):

    print("+++++++++++++++++++++++++++++++++")
    print(f"{com.name:>9}: {" ".join([str(i) for i in com.card]) :<16}-> {com_score}")
    print(f"{player.name:>9}: {" ".join([str(i) for i in player.card]) :<16}-> {player_score}")

    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

    if com_score == player_score:
        print(f"Draw!")
    elif com.check_blackjack() and player.check_blackjack():
        print(f"Draw!")
    
    elif com.check_blackjack() and not player.check_blackjack():print(f"{com.name} wins.")
    elif not com.check_blackjack() and  player.check_blackjack():print(f"{player.name} wins.")



    elif (com_score > player_score and com_score <= 21) or (com_score <= 21 and player_score > 21) or (com.check_blackjack() and not player.check_blackjack()):
        print(f"{com.name} wins.")
    elif (player_score > com_score and player_score <= 21) or (com_score > 21 and player_score <= 21) or (not com.check_blackjack() and player.check_blackjack()):
        print(f"{player.name} wins.")        
        
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")

#==============================================Submist this block (end) ==============================================


def play(player1='Computer', player2='Player', d=None, RENDER=False):
    print('Welcome to MikeLab BlackJack Casino.')
    preamble(RENDER)
    # create a deck of cards
    if d==None:
        deck = Deck()
        deck.reset()
    else:

        deck = createVirtualDeck(d)

#==============================================Submist this block (start) ==============================================

    p1 = myCard(name=player1)
    p2 = myCard(name=player2)

    p1.get_card(deck.get_card())
    p2.get_card(deck.get_card())
    p1.get_card(deck.get_card())
    p2.get_card(deck.get_card())

    p1.print_hidden()
    p2.print_normal()

    while True:
        if len(p2.card) == 5 :break
        if p2.score >= 21:break
        input_val = input("Draw another card (y/n): ")
        if input_val.lower() == 'y':
            p2.get_card(deck.get_card())
            p2.print_normal()
        else:
            break

    while True:
        if len(p1.card) == 2:
            if p1.score == 21:
                break
            else: 
                p1.get_card(deck.get_card())
                continue
        if p1.checkEndGame():break
        if p1.get_more_card(p2.score, len(p2.card)):
            p1.get_card(deck.get_card())
            continue
        break
    
    print_result(p1, p2, p1.score, p2.score)
    
#==============================================Submist this block (end) ==============================================


def testcase01():
    random.seed(2)
    play()
def testcase02():
    random.seed(16)
    play()
def testcase03():
    random.seed(30)
    play()
def testcase04():
    s = 'K♣ Q♠ A♣ 3♥ 2♠ 6♥ 8♥ 9♥ J♠ 4♦ 2♥ 9♠'
    play('Toto', 'Tutu', d=s)

def testcase05():
    s = 'A♣ 3♥ 2♠ T♥ 8♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase06():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase07():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ 2♥ T♠'
    play(d=s)
def testcase08():
    s = '4♠ A♥ A♣ 3♥ 2♠ 4♥ 5♥ A♠ A♦ Q♥ 3♠'
    play(d=s)
def testcase09():
    s = '5♠ A♥ A♣ 8♥ J♠ 4♥ 5♥ A♠ A♦ 2♥ 3♠'
    play(d=s)
def testcase10():
    s = 'A♣ 3♦ A♦ A♥ 3♥ 4♣ 4♥ 7♣ 3♣ 2♦ A♠'
    play(d=s)
#------------------------------------------
q = int(input())
if q==1:
    testcase01()
elif q==2:
    testcase02()
elif q==3:
    testcase03()
elif q==4:
    testcase04()
elif q==5:
    testcase05()
elif q==6:
    testcase06()
elif q==7:
    testcase07()
elif q==8:
    testcase08()
elif q==9:
    testcase09()
elif q==10:
    testcase10()