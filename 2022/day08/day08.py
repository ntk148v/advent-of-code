import os

from aocclient.client import Client

ans1 = ans2 = 0


with open(os.path.join(os.getcwd(), "input.txt")) as f:
    trees = f.read().strip().split('\n')
    trees = [list(map(int, t)) for t in trees]

    for i in range(0, len(trees)):
        # All trees around the edge are visible
        if i == 0 or i == (len(trees) - 1):
            ans1 += len(trees[i])
            continue

        for j in range(0, len(trees[i])):
            # All trees around the edge are visible
            if j == 0 or j == (len(trees[i]) - 1):
                ans1 += 1
                continue
            cols = [k[j] for k in trees]
            if trees[i][j] > max(trees[i][j+1:]) or trees[i][j] > max(trees[i][:j]) \
                    or trees[i][j] > max(cols[i+1:]) or trees[i][j] > max(cols[:i]):
                ans1 += 1

    print("Part 1: ", ans1)
#     print("Part 2: ", ans2)

cli = Client(year=2022, day=8)
# cli.submit_answer(1, ans1)
# cli.submit_answer(2, ans2)
