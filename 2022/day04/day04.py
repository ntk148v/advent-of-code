import os

from aocclient.client import Client

ans1 = ans2 = 0

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    pairs = f.read().strip().split('\n')
    for pair in pairs:
        pair = [tuple(map(int, p.split('-'))) for p in pair.split(',')]
        # Part 1
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or \
                (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]):
            ans1 += 1

        # Part 2
        overlap = set(range(pair[0][0], pair[0][1]+1)) & set(
            range(pair[1][0], pair[1][1]+1))
        if len(overlap) > 0:
            ans2 += 1

    print("Part 1: ", ans1)
    print("Part 2: ", ans2)

cli = Client(year=2022, day=4)
cli.submit_answer(1, ans1)
cli.submit_answer(2, ans2)
