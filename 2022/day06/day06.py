import collections
import os

from aocclient.client import Client

cli = Client(year=2022, day=6)
cli.setup()

ans1 = None
ans2 = None

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    buffer = f.read().split('\n')[0]
    # Simple solution
    for i, v in enumerate(buffer):
        if len(buffer[i:i+4]) == len(set(buffer[i:i+4])):
            ans1 = i+4
            break
    print("Part 1: ", ans1)
    cli.submit_answer(1, ans1)

    for i, v in enumerate(buffer):
        if len(buffer[i:i+14]) == len(set(buffer[i:i+14])):
            ans2 = i+14
            break
    print("Part 2: ", ans2)
    cli.submit_answer(1, ans2)
