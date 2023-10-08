#!/usr/bin/env python3

def get_result(player_a, player_b):
    all_wins = {
        ("rock", "scissors"): "crushes",
        ("paper", "rock"): "covers",
        ("scissors", "paper"): "cuts"
    }
    if player_a == player_b:
        return f"Both did {player_a}. They tied."
    elif (player_a, player_b) in all_wins:
        verb = all_wins[(player_a, player_b)]
        return f"{player_a} {verb} {player_b}! player A wins."
    else:
        verb = all_wins[(player_b, player_a)]
        return f"{player_b} {verb} {player_a}! player B wins."

def fix_capitalization(astring):
    end_of_sentence_punc = ".?!"
    newchars = []
    # Treat first char as if follows a "."
    prevnonspacechar = "."
    for char in astring:
        newchar = char
        if prevnonspacechar in end_of_sentence_punc:
            newchar = char.upper()
        newchars.append(newchar)
        if not char.isspace():
            prevnonspacechar = char
    newstring = "".join(newchars)
    return newstring

if __name__ == '__main__':
    choices = ["rock", "paper", "scissors"]
    for aaa in choices:
        for bbb in choices:
            print(fix_capitalization(get_result(aaa, bbb)))
