import os

from aocclient.client import Client

ans1 = None
ans2 = None

# {direction: (deltax, deltay)}
delta = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    motions = f.read().strip().split('\n')
    # This is a rope with 10 knots (part 2)
    rope = [(0, 0)] * 10
    # Tail positions
    tail_pos_1 = {(0, 0)}
    tail_pos_2 = {(0, 0)}

    for motion in motions:
        direction, steps = motion.split()
        steps = int(steps)

        for _ in range(steps):
            hx, hy = rope[0]
            dx, dy = delta[direction]

            # Move the head
            rope[0] = hx+dx, hy+dy
            for i in range(9):
                # consider this is head
                hx, hy = rope[i]
                # the one after is tail
                tx, ty = rope[i+1]

                dx, dy = hx-tx, hy-ty
                if dx**2 + dy**2 > 2:
                    if dx != 0:
                        tx += 1 if dx > 0 else -1
                    if dy != 0:
                        ty += 1 if dy > 0 else -1
                    rope[i+1] = tx, ty

            # Keep track
            tail_pos_1.add(rope[1])
            tail_pos_2.add(rope[9])

ans1 = len(tail_pos_1)
print("Part 1: ", ans1)

ans2 = len(tail_pos_2)
print("Part 2: ", ans2)
cli = Client(year=2022, day=9)
cli.submit_answer(1, ans1)
cli.submit_answer(2, ans2)
