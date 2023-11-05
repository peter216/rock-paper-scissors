#!/usr/bin/env python3
import random

class RPS():
    all_wins = {
        ("rock", "scissors"): "crushes",
        ("rock", "lizard"): "crushes",
        ("paper", "rock"): "covers",
        ("paper", "Spock"): "disproves",
        ("scissors", "paper"): "cuts",
        ("scissors", "lizard"): "decapitates",
        ("Spock", "scissors"): "smashes",
        ("Spock", "rock"): "vaporizes",
        ("lizard", "paper"): "eats",
        ("lizard", "Spock"): "poisons",
    }
    def __init__(self, entry):
        self.entry = entry
    def __repr__(self):
        return self.entry
    def cap(self):
        return self.entry.capitalize()
    def fights(self, other):
        if verb := RPS.all_wins.get((self.entry, other.entry)):
            return f"{self.cap()} {verb} {other}! You win!"
        elif verb := RPS.all_wins.get((other.entry, self.entry)):
            return f"{other.cap()} {verb} {self}! Computer wins!"
        else:
            return f"You tied."


if __name__ == '__main__':
    choices = {"r": "rock",
               "p": "paper",
               "s": "scissors",
               "l": "lizard",
               "k": "Spock"}
    while True:
        print()
        aaa = input("(r)ock/(p)aper/(s)cissors/(l)izard/Spoc(k)/(q)uit? ").lower().strip()
        fchar = aaa[0] if len(aaa) else "0"
        if fchar == 'q':
            break
        elif aaa := choices.get(fchar):
            bbb = random.choice(list(choices.values()))
            print(f"You chose {aaa}.")
            print(f"Computer did {bbb}.")
            print(RPS(aaa).fights(RPS(bbb)))
        else:
            print("Invalid choice. Try again.")
