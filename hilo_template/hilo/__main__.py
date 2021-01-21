#Hilo team challenge 4
# TODO: Add entry point code here
# *must write atleast two classes
# *Each module, class and method must have a corresponding comment using the style demonstrated in the solo checkpoint.
# *The game must remain generally true to the order of play described in the rules.
#
# other options
#Enhanced input validation with user-friendly messages.
#Enhanced game play and game over messages.
#Enhanced card representation (incorporate Jack, Queen, King and Ace)
#Enhanced game display (e.g. different colors for correct or incorrect guesses)

import random

class rand_card:
    #creates random card

    def __init__(self):
        self.card = 0
    
    def next_card(self):
        card = random.randint(1,13)
        #print(f"The card is: {card}")
        return card

class comp_card:
    #compares past card with new card

    def __init__(self):
        self.card1 = 0
        self.card2 = 0
        self.score = 300
        self.rand = rand_card()
        self.play = True


    def start_game(self):
        while (self.play):
            if (self.card2 == 0):
                self.card1 = self.rand.next_card()
                print(f"The card is: {self.card1}")
                x = input("Higher or lower? [h/l] ")
                self.card2 = self.rand.next_card()
                print(f"Next card was: {self.card2}")
                if (x == "h") & (self.card1 < self.card2) | (x == "l") & (self.card1 > self.card2):
                    self.score += 100
                    print(f"Your score is: {self.score}")
                    self.keep_play()
                    #break
                else:
                    self.score -= 75
                    print(f"Your score is: {self.score}")
                    self.keep_play()
                    #break
            else:
                self.card1 = self.card2
                print(f"The card is: {self.card1}")
                x = input("Higher or lower? [h/l] ")
                self.card2 = self.rand.next_card()
                print(f"Next card was: {self.card2}")
                if (x == "h") & (self.card1 < self.card2) | (x == "l") & (self.card1 > self.card2):
                    self.score += 100
                    print(f"Your score is: {self.score}")
                    self.keep_play()
                    #break
                else:
                    self.score -= 75
                    print(f"Your score is: {self.score}")
                    self.keep_play()

    def keep_play(self):
        y = input("Keep playing? [y/n] ")
        if (y == "y"):
            self.play = True
            print()
        else:
            self.play = False
            print()
            print(f"Your Final score is: {self.score}")



hilo = comp_card()
hilo.start_game()

