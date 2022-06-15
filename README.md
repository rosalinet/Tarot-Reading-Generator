<h2 align="center">
  <img width="45" src="https://media.discordapp.net/attachments/736460753435099226/823278038338895902/image1.webp">
  Tarot Reading Generator
  <img width="45" src="https://user-images.githubusercontent.com/92281462/158006004-41d49594-d7fa-40dc-8719-12cfa9811499.png">
</h2>

<p align="center">
  This is a Tarot Reading Generator made by me, Rose! <br>
  <img width="300" src="https://cdn.discordapp.com/attachments/772198618069073929/788989408799359017/image0.png"> <br>
I initially typed all of the Major Arcana cards, their symbolism, AND advice in a spreadsheet and planned on using pandas to manipulate the data in python... but after typing so much for the major arcana alone, I got super lazy. And what do programmers do when they feel super lazy? See if someone else has done it before them! So I stumbled upon <a href="https://github.com/ekelen/tarot-api/blob/master/static/card_data.json">this JSON file</a> made by ekelen here on github. It had ALL 78 cards (Major and Minor Arcana) with their types, meanings, REVERSED meanings, and even descriptions of how the cards look! I edited parts of the JSON file (mostly just meanings) to fit the intention of my code more. <br>
<img width="300" src="https://cdn.discordapp.com/attachments/772198618069073929/788989408799359017/image0.png"> <br>
The meat of the code is in python, but I think I may make a cute HTML frontend for it one day. The comments aren't the best, but the code itself is very small. I use a random generator to pick a number between 0-77 (78 cards) to choose the corresponding card and then print out it's meaning. I still want to continue editing the JSON file a bit to fit how I interpret the cards, and I'd like to implement an "advice" feature for every particular card in the future. <br>
<img width="300" src="https://cdn.discordapp.com/attachments/772198618069073929/788989408799359017/image0.png"> <br>
 At the moment, the reading generator only generates one spread: the past, present, and future spread.
<br>About the past, present, and future spread:
<br> ✧ The first card represents elements from the past that AFFECT your current situation.
<br> ✧ The second card describes the current STATUS of the situation.
<br> ✧ The third card gives insight into a POSSIBLE OUTCOME of the situation.
<br>Then the user can type 'draw' or 'exit' to keep drawing more spreads or exit the instance.
</p>
<p align = "center">
<img width="500" src="https://cdn.discordapp.com/attachments/772198618069073929/785927303770669096/image0.png">
</p>




<br>
Disclaimers~

I wanted to make this because I have a tarot card set that I really enjoy using every once in awhile. I personally use them as general guidance when I feel I'm a little lost or confused, but I understand that they don't provide any concrete information. Honestly for me, they are also mostly just for fun. I am aware that the crossover of spirituality and technology can be pretty counterintuitive, but I am involved in both, enjoy both, and can appreciate both.


This is a personal project I've been working on with some help from my little sister! It is still in the works, but I will only update *working* versions of the code. 
