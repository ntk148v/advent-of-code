import os

from aocclient.client import Client

ans1 = None
ans2 = None

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    motions = f.read().strip().split('\n')
    # begin at the starting position
    head = (0, 0)
    tail = (0, 0)
    seen = {(0, 0)}

    for motion in motions:
        direction, steps = motion.split()
        steps = int(steps)

        for _ in range(steps):
            if direction == 'D':
                head = head[0], head[1]+1
            elif direction == 'U':
                head = head[0], head[1]-1
            elif direction == 'R':
                head = head[0]+1, head[1]
            elif direction == 'L':
                head = head[0]-1, head[1]

            delta = head[0]-tail[0], head[1]-tail[1]

            # https://en.wikipedia.org/wiki/Euclidean_distance
            if delta[0]**2 + delta[1]**2 > 2:
                if delta[0] > 0:
                    tail = tail[0]+1, tail[1]
                elif delta[0] < 0:
                    tail = tail[0]-1, tail[1]
                if delta[1] > 0:
                    tail = tail[0], tail[1]+1
                elif delta[1] < 0:
                    tail = tail[0], tail[1]-1
                seen.add(tail)

ans1 = len(seen)
print("Part 1: ", ans1)
# print("Part 2: ", ans2)
cli = Client(year=2022, day=9)
# cli.submit_answer(1, ans1)
# cli.submit_answer(2, ans2)
