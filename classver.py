#!/usr/bin/env python3

class RPS():
    def __init__(self, entry):
        self.entry = entry
    def __repr__(self):
        return self.entry
    def cap(self):
        return self.entry.capitalize()
    def fights(self, other):
        all_wins = {
            ("rock", "scissors"): "crushes",
            ("paper", "rock"): "covers",
            ("scissors", "paper"): "cuts"
        }
        if verb := all_wins.get((self.entry, other.entry)):
            return f"{self.cap()} {verb} {other}! Player A wins!"
        elif verb := all_wins.get((other.entry, self.entry)):
            return f"{other.cap()} {verb} {self}! Player B wins!"
        else:
            return f"Both did {self}. They tied."


if __name__ == '__main__':
    choices = ["rock", "paper", "scissors"]
    for aaa in choices:
        for bbb in choices:
            print(RPS(aaa).fights(RPS(bbb)))
