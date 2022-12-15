import os

from aocclient.client import Client

ans1 = None
ans2 = None

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    print("Part 1: ", ans1)
    print("Part 2: ", ans2)

cli = Client(year=2022, day=9)
cli.submit_answer(1, ans1)
cli.submit_answer(2, ans2)
