#!/usr/bin/python3
import os

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    chunks = f.read().split('\n\n')
    chunks = [tuple(map(int, chunk.split())) for chunk in chunks]
    chunks.sort(key=sum, reverse=True)

    print("Part 1: ", sum(chunks[0]))
    print("Part 2: ", sum(map(sum, chunks[:3])))
