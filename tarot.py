
from flask import Blueprint, render_template, flash, redirect, Markup
import json
import random



#Open JSON file of tarot card info, courtesy of ekelen @ https://github.com/ekelen/tarot-api
with open('card_info.json') as json_file:
        data = json.load(json_file)
        deck = data['cards']

#This class constructs a card from the deck created from the JSON file
class Card:
    def __init__(self):
        self.card = deck[random.randint(0,77)]
        self.name = self.card['name']
        self.type = self.card['type']
        self.desc = self.card['desc']
        if random.randint(0,2) == 0:
            self.meaning = self.card['meaning_up']
            self.orientation = "(Right Side Up)"
        else:
            self.meaning = self.card['meaning_rev']
            self.orientation = "(Reversed)"

    #Prints out the card name & orientation
    def print_cardname(self):
        return(f'{self.name} {self.orientation}')
    
    #Prints out the card meaning (orientation-dependent)
    def print_meaning(self):
         return(f'This card typically stands for: {self.meaning}')




tarot = Blueprint(__name__, "tarot")
divider = Markup("<div>─── ･ ｡ﾟ☆: *.☽.* :☆ﾟ. ───</div>")

@tarot.route("/")
def home():
    return render_template("index.html")

@tarot.route("/ppf", methods=["POST","GET"])
def ppf_gen():
    flash("Your FIRST card representing INSIGHT into the PAST of the situation is:")
    past_card = Card()
    flash(past_card.print_cardname())
    flash(past_card.print_meaning())
    flash(divider)
    flash("Your SECOND card representing the CURRENT STATUS of the situation is:")
    present_card = Card()
    flash(present_card.print_cardname())
    flash(present_card.print_meaning())
    flash(divider)
    flash("Your LAST card representing a POSSIBLE OUTCOME of the situation is:")
    future_card = Card()
    flash(future_card.print_cardname())
    flash(future_card.print_meaning())
    return render_template("draw.html")

@tarot.route("/mbs", methods=["POST","GET"])
def mbs_gen():
    flash("mbs")
    return render_template("draw.html")

@tarot.route("/homepage_redirect", methods=["POST"])
def return_home():
    return redirect("/tarot")





