import copy
import os
import re

from aocclient.client import Client

cli = Client(year=2022, day=5)
cli.setup()

stacks_1 = {}

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    raw_stacks, raw_procedure = f.read().split('\n\n')
    # Process raw input
    raw_stacks = [i for i in raw_stacks.strip().split('\n')]
    # Init stacks
    stacks_1 = {int(k): [] for k in raw_stacks.pop().split()}

    # Process - ugly but it works!
    for r in raw_stacks:
        tmp = []
        for c in range(0, len(r), 4):
            tmp.append(r[c:c+3])
        for i, v in enumerate(tmp):
            e = v.strip().strip(']').strip('[')
            if not e:
                continue
            stacks_1[i+1].insert(0, e)
    stacks_2 = copy.deepcopy(stacks_1)
    print("Before: ", stacks_2)

    procedure = [re.findall(r'\d+', i)
                 for i in raw_procedure.strip().split('\n')]
    # Follow procedure
    for r in procedure:
        # Format [nums, src, dst]
        # Part 1
        crates = stacks_1[int(r[1])][-int(r[0]):]
        crates.reverse()
        stacks_1[int(r[2])] += crates
        stacks_1[int(r[1])] = stacks_1[int(r[1])][:-int(r[0])]
        # Part 2
        stacks_2[int(r[2])] += stacks_2[int(r[1])][-int(r[0]):]
        stacks_2[int(r[1])] = stacks_2[int(r[1])][:-int(r[0])]
    print("After: ", stacks_2)
    result1 = ''.join([v[-1] for v in stacks_1.values()])
    print("Part 1: ", result1)
    cli.submit_answer(1, result1)
    result2 = ''.join([v[-1] for v in stacks_2.values()])
    print("Part 2: ", result2)
    cli.submit_answer(1, result2)
