import os

from aocclient.client import Client

ans1 = None
ans2 = None

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    # get list of instructions
    program = f.read().strip().split('\n')
    cycle = 1
    X = 1
    total = 0
    crt = ''

    for instr in program:
        instr = instr.split()

        if X <= cycle % 40 <= X+2:
            crt += '#'
        else:
            crt += '.'

        cycle += 1  # noop
        if len(instr) == 2:  # addx V
            # calculate signal strength
            if cycle % 40 == 20:
                total += cycle * X
            elif cycle % 40 == 1:
                crt += '\n'

            if X <= cycle % 40 <= X+2:
                crt += '#'
            else:
                crt += '.'

            # register X
            cycle += 1
            X += int(instr[1])

        if cycle % 40 == 20:
            total += cycle * X
        elif cycle % 40 == 1:
            crt += '\n'

    ans1 = total
    print(crt) # Don't know how to convert to string to auto submit
    # result look like this - ELPLZGZL
    ####.#....###..#....####..##..####.#...#
    #....#....#..#.#.......#.#..#....#.#....
    ###..#....#..#.#......#..#......#..#....
    #....#....###..#.....#...#.##..#...#...#
    #....#....#....#....#....#..#.#....#....
    ####.####.#....####.####..###.####.####.
    print("Part 1: ", ans1)
    ans = 'ELPLZGZL'
    print("Part 2: ", ans2)

cli = Client(year=2022, day=10)
cli.submit_answer(1, ans1)
cli.submit_answer(2, ans2)
