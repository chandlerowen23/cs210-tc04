from game.rand_card import rand_card


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

                #Prompting user
                x = input("Higher or lower? [h/l] ")
                self.card2 = self.rand.next_card()
                print(f"Next card was: {self.card2}")

                #Comparing Next card is either greater or not, it is a positive result so increment score plus 100
                if (x == "h") & (self.card1 < self.card2) | (x == "l") & (self.card1 > self.card2):
                    self.score += 100
                    print(f"Your score is: {self.score}")
                    #calling some functions
                    self.score_cero()
                    self.keep_play()
                    #break
                else:
                    self.score -= 75
                    print(f"Your score is: {self.score}")
                    self.score_cero()
                    self.keep_play()
                    #break

            #Starting again taking last 'Next card' as 'The card'
            else:
                self.card1 = self.card2
                print(f"The card is: {self.card1}")
                x = input("Higher or lower? [h/l] ")
                self.card2 = self.rand.next_card()
                print(f"Next card was: {self.card2}")

                # Comparing Next card is either greater or not, it is a positive result so increment score plus 100
                if (x == "h") & (self.card1 < self.card2) | (x == "l") & (self.card1 > self.card2):
                    self.score += 100
                    print(f"Your score is: {self.score}")
                    self.score_cero()
                    self.keep_play()
                    #break
                else:
                    self.score -= 75
                    print(f"Your score is: {self.score}")
                    self.score_cero()
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
            
    def score_cero(self):
        if self.score == 0:
            print('Game Over')
            self.play = False
            exit()
        else:
            pass

