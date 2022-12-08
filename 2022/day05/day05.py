import os
import re

from aocclient.client import Client

cli = Client(year=2022, day=5)
cli.setup()

stacks = {}

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    raw_stacks, raw_procedure = f.read().split('\n\n')
    # Process raw input
    raw_stacks = [i for i in raw_stacks.strip().split('\n')]
    # Init stacks
    stacks = {int(k): [] for k in raw_stacks.pop().split()}

    # Process - ugly but it works!
    for r in raw_stacks:
        tmp = []
        for c in range(0, len(r), 4):
            tmp.append(r[c:c+3])
        for i, v in enumerate(tmp):
            e = v.strip().strip(']').strip('[')
            if not e:
                continue
            stacks[i+1].insert(0, e)
    print("Before: ", stacks)

    procedure = [re.findall(r'\d+', i)
                 for i in raw_procedure.strip().split('\n')]
    # Follow procedure
    for r in procedure:
        # Format [nums, src, dst]
        crates = stacks[int(r[1])][-int(r[0]):]
        crates.reverse()
        stacks[int(r[2])] += crates
        stacks[int(r[1])] = stacks[int(r[1])][:-int(r[0])]
    print("After: ", stacks)
    result1 = ''.join([v[-1] for v in stacks.values()])
    print("Part 1: ", result1)
    cli.submit_answer(1, result1)
