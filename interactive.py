#!/usr/bin/env python3
import random

class RPS():
    def __init__(self, entry):
        self.entry = entry
    def __repr__(self):
        return self.entry.capitalize()
    def fights(self, other):
        all_wins = {
            ("rock", "scissors"): "crushes",
            ("paper", "rock"): "covers",
            ("scissors", "paper"): "cuts"
        }
        if verb := all_wins.get((self.entry, other.entry)):
            return f"{self} {verb} {other}! You win!"
        elif verb := all_wins.get((other.entry, self.entry)):
            return f"{other} {verb} {self}! Computer wins!"
        else:
            return f"Both did {self}. You tied."


if __name__ == '__main__':
    choices = {"r": "rock",
               "p": "paper",
               "s": "scissors"}
    while True:
        print()
        aaa = input("Rock/Paper/Scissors/Quit? ").lower().strip()
        fchar = aaa[0] if len(aaa) else "0"
        if fchar == 'q':
            break
        elif aaa := choices.get(fchar):
            bbb = random.choice(list(choices.values()))
            print(RPS(aaa).fights(RPS(bbb)))
        else:
            print("Invalid choice  Try again.")
