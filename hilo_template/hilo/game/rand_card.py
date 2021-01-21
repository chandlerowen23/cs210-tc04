#rand_card Class

import random

class rand_card:
    #creates random card

    def __init__(self):
        self.card = 0
    
    def next_card(self):
        card = random.randint(1,13)
        #print(f"The card is: {card}")
        return card
