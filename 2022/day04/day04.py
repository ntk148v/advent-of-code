import os

count1 = count2 = 0

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    pairs = f.read().strip().split('\n')
    for pair in pairs:
        pair = [tuple(map(int, p.split('-'))) for p in pair.split(',')]
        # Part 1
        if (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]) or \
                (pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]):
            count1 += 1

        # Part 2
        overlap = set(range(pair[0][0], pair[0][1]+1)) & set(
            range(pair[1][0], pair[1][1]+1))
        if len(overlap) > 0:
            count2 += 1

    print("Part 1: ", count1)
    print("Part 2: ", count2)
