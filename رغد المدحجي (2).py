## "Spider Solitaire" 



### كود اللعبة


import tkinter as tk
import random

# تعريف صف واحد من الأوراق
SUITS = ['♥', '♦', '♣', '♠']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# إنشاء الأوراق
def create_deck():
    return [(rank, suit) for suit in SUITS for rank in RANKS]

# خلط الأوراق
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# إنشاء واجهة اللعبة
class SpiderSolitaire:
    def __init__(self, root):
        self.root = root
        self.root.title("لعبة سوليتر العنكبوت")
        self.deck = shuffle_deck(create_deck())
        self.create_interface()

    def create_interface(self):
        self.canvas = tk.Canvas(self.root, width=600, height=400, bg="green")
        self.canvas.pack()

        self.draw_deck()

    def draw_deck(self):
        for i in range(len(self.deck)):
            card = self.deck[i]
            x = (i % 13) * 40 + 20
            y = (i // 13) * 100 + 20
            self.canvas.create_text(x, y, text=f"{card[0]}{card[1]}", font=("Arial", 14))

# تشغيل اللعبة
if __name__ == "__main__":
    root = tk.Tk()
    game = SpiderSolitaire(root)
    root.mainloop()

