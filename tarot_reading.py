import json
import random

#Open JSON file of tarot card info, courtesy of ekelen @ https://github.com/ekelen/tarot-api
with open('card_info.json') as json_file:
        data = json.load(json_file)
        deck = data['cards']

#This class constructs a card from the deck created from the JSON file
class Card:
    def __init__(self):
        self.card = deck[random.randint(0,78)]
        self.name = self.card['name']
        self.type = self.card['type']
        self.desc = self.card['desc']
        if random.randint(0,2) == 0:
            self.meaning = self.card['meaning_up']
            self.orientation = "(Right Side Up)"
        else:
            self.meaning = self.card['meaning_rev']
            self.orientation = "(Reversed)"

    #Prints out the card details in a nice format
    def print_reading(self):
        print(f'The card drawn was: {self.name} {self.orientation}.')
        print(f'This card typically stands for: {self.meaning}.')



class Main:
    def main():
        print('''
            ╭── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ──╮
            Welcome to the Tarot Reading generator created by your fellow witch, Rose!
            (To leave at any time, just type 'EXIT')
            ─── ･ ｡ﾟ☆: *.☽ .* :☆ﾟ. ───
            At the moment, we only have one spread available: 
            ・❥・ 'The past, present, and future of a particular situation's spread
             ✧ The first card represents elements from the past that AFFECT your current situation.
             ✧ The second card describes the current STATUS of the situation.
             ✧ The third card gives insight into a POSSIBLE OUTCOME of the situation.
            To start, first think of a current situation in your life...
            ╰── ⋅ ⋅ ── ✩ ── ⋅ ⋅ ──╯''')

        user_choice = input('\nWhen you are ready, type DRAW: ').lower()
        while(user_choice != 'exit'):
            
            if(user_choice == 'draw'):
                
                print(". . • ☆ . ° .• °:. *₊ ° . ☆")
                print("Your first card representing the past of the situation is being drawn...")
                past_card = Card()
                past_card.print_reading()
                print(". . • ☆ . ° .• °:. *₊ ° . ☆")
                print("Your second card representing the present of the situation is being drawn...")
                present_card = Card()
                present_card.print_reading()
                print(". . • ☆ . ° .• °:. *₊ ° . ☆")
                print("Your first card representing a possible future of the situation is being drawn...")
                future_card = Card()
                future_card.print_reading()
                print(". . • ☆ . ° .• °:. *₊ ° . ☆")
                user_choice = input("\nType draw to generate another reading or exit to leave ➤")
            
            else:
                print("That is an invalid input! Please try again.")
                user_choice = input('If you\'d like a reading, type DRAW; Otherwise, you can leave by typing EXIT: ').lower()
            
        print("Thank you for using the Tarot Reading Generator. See you next time!")
        exit



    
    if __name__ == "__main__":
        main()

