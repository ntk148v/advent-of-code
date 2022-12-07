import os

# Convert a list of character to number and return sum


def convert(items):
    s = 0
    for i in items:
        if i.isupper():
            s += ord(i)-ord('A') + 27
        else:
            s += ord(i)-ord('a')+1
    return s


s1 = s2 = 0

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    ruckpacks = f.read().strip().split('\n')
    for ruckpack in ruckpacks:
        items = (set(ruckpack[:len(ruckpack)//2]) &
                 set(ruckpack[len(ruckpack)//2:]))
        s1 += convert(items)
    print("Part 1: ", s1)
    for i in range(0, len(ruckpacks), 3):
        items = (set(ruckpacks[i]) & set(ruckpacks[i+1]) & set(ruckpacks[i+2]))
        s2 += convert(items)
    print("Part 2: ", s2)
