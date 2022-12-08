#!/usr/bin/python3
import os

from aocclient.client import Client

cli = Client(year=2022, day=2)
cli.setup()

m1 = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

m2 = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

score1 = 0
score2 = 0

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    rounds = f.read().strip().split('\n')
    for round in rounds:
        round = round.split()
        # Handle part 1
        result = m1[round[1]] - m1[round[0]]
        if result == 0:
            score1 += (3+m1[round[1]])  # draw
        elif result == -1 or result == 2:
            score1 += m1[round[1]]  # lose
        elif result == -2 or result == 1:
            score1 += (6+m1[round[1]])  # win

        # Handle part 2
        score2 += m2[round[1]]
        if m2[round[1]] == 0:
            if m1[round[0]] == 1:
                score2 += 3
            elif m1[round[0]] == 2:
                score2 += 1
            elif m1[round[0]] == 3:
                score2 += 2
        elif m2[round[1]] == 3:
            score2 += m1[round[0]]
        elif m2[round[1]] == 6:
            if m1[round[0]] == 1:
                score2 += 2
            elif m1[round[0]] == 2:
                score2 += 3
            elif m1[round[0]] == 3:
                score2 += 1
    print("Part 1: ", score1)
    cli.submit_answer(1, score1)
    print("Part 2: ", score2)
    cli.submit_answer(2, score2)
