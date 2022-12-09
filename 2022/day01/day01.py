import os

from aocclient.client import Client

ans1 = None
ans2 = None

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    chunks = f.read().split('\n\n')
    chunks = [tuple(map(int, chunk.split())) for chunk in chunks]
    chunks.sort(key=sum, reverse=True)
    ans1 = sum(chunks[0])
    ans2 = sum(map(sum, chunks[:3]))


cli = Client(year=2022, day=1)
cli.submit_answer(1, ans1)
cli.submit_answer(2, ans2)
