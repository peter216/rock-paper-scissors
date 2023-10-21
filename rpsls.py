#!/usr/bin/env python3

class RPS():
    def __init__(self, entry):
        self.entry = entry
    def __repr__(self):
        return self.entry.capitalize()
    def fights(self, other):
        all_wins = {
            ("rock", "scissors"): "crushes",
            ("rock", "lizard"): "crushes",
            ("paper", "rock"): "covers",
            ("paper", "spock"): "disproves",
            ("scissors", "paper"): "cuts",
            ("scissors", "lizard"): "decapitates",
            ("spock", "scissors"): "smashes",
            ("spock", "rock"): "vaporizes",
            ("lizard", "paper"): "eats",
            ("lizard", "spock"): "poisons",
        }
        if verb := all_wins.get((self.entry, other.entry)):
            return f"{self} {verb} {other}! Player A wins!"
        elif verb := all_wins.get((other.entry, self.entry)):
            return f"{other} {verb} {self}! Player B wins!"
        else:
            return f"Both did {self}. They tied."


if __name__ == '__main__':
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    for aaa in choices:
        for bbb in choices:
            print(RPS(aaa).fights(RPS(bbb)))
