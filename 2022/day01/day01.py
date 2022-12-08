import os

from aocclient.client import Client

cli = Client(year=2022, day=1)
cli.setup()

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    chunks = f.read().split('\n\n')
    chunks = [tuple(map(int, chunk.split())) for chunk in chunks]
    chunks.sort(key=sum, reverse=True)

    print("Part 1: ", sum(chunks[0]))
    cli.submit_answer(1, sum(chunks[0]))
    print("Part 2: ", sum(map(sum, chunks[:3])))
    cli.submit_answer(2, sum(map(sum, chunks[:3])))
