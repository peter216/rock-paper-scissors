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
            return (0, f"{self.cap()} {verb} {other}! You win!")
        elif verb := RPS.all_wins.get((other.entry, self.entry)):
            return (1, f"{other.cap()} {verb} {self}! Computer wins!")
        else:
            return (2, f"You tied.")


if __name__ == '__main__':
    choices = {"r": "rock",
               "p": "paper",
               "s": "scissors",
               "l": "lizard",
               "k": "Spock"}
    score = [0, 0, 0]
    while True:
        print()
        aaa = input("(r)ock/(p)aper/(s)cissors/(l)izard/Spoc(k)/(q)uit? ").lower().strip()
        fchar = aaa[0] if len(aaa) else "0"
        if fchar == 'q':
            wins, losses, ties = score
            if wins >= losses:
                print("Good game.")
            else:
                print("Better luck next time.")
            break
        elif aaa := choices.get(fchar):
            bbb = random.choice(list(choices.values()))
            print(f"You chose {aaa}.")
            print(f"Computer did {bbb}.")
            augment_index, verbiage = RPS(aaa).fights(RPS(bbb))
            print(verbiage)
            score[augment_index] += 1
            wins, losses, ties = score
            print(f"Score: {wins} wins, {losses} losses, {ties} ties")
        else:
            print("Invalid choice. Try again.")
