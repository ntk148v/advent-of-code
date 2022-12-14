import copy
import os

from aocclient.client import Client

ans1 = ans2 = 0


def calc_scenic_score(curr, trees):
    """Calculate scenic score by direction

    :param curr: the current tree
    :param trees: the list of trees by direction (up, down, left, top)
    """
    scenic_score = 1
    for i, t in enumerate(trees):
        if t >= curr or i == (len(trees)-1):
            break
        scenic_score += 1
    return scenic_score


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
            # Part 1
            if trees[i][j] > max(trees[i][j+1:]) or trees[i][j] > max(trees[i][:j]) \
                    or trees[i][j] > max(cols[i+1:]) or trees[i][j] > max(cols[:i]):
                ans1 += 1

            # Part 2
            left = trees[i][j+1:]
            right = copy.copy(trees[i][:j])
            right.reverse()
            bottom = cols[i+1:]
            top = copy.copy(cols[:i])
            top.reverse()
            # Calclulate
            left = calc_scenic_score(trees[i][j], left)
            right = calc_scenic_score(trees[i][j], right)
            bottom = calc_scenic_score(trees[i][j], bottom)
            top = calc_scenic_score(trees[i][j], top)
            scenic_score = left * top * right * bottom
            if scenic_score > ans2:
                ans2 = scenic_score

print("Part 1: ", ans1)
print("Part 2: ", ans2)
cli = Client(year=2022, day=8)
cli.submit_answer(1, ans1)
cli.submit_answer(2, ans2)
