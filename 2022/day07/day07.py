from collections import deque, defaultdict
import os
import pathlib

from aocclient.client import Client

cli = Client(year=2022, day=7)

ans1 = 0
ans2 = None


def calculate_size(fs, path):
    size = 0
    for f in fs[path]:
        if isinstance(f, pathlib.Path):
            size += calculate_size(fs, f)
        else:
            size += int(f)
    return size


with open(os.path.join(os.getcwd(), "input.txt")) as f:
    lines = deque(f.read().strip().split('\n'))
    fs = defaultdict(list)
    curr = None

    while lines:
        line = lines.popleft().split()
        command = line[1]
        args = line[2:]

        if command == "ls":
            # List of directory contents, keep going until
            # run out of lines or the next line is a command
            while lines and not lines[0].startswith('$'):
                # Get the size of the file
                size = lines.popleft().split()[0]

                if size == 'dir':
                    continue

                fs[curr].append(int(size))
        else:
            # Change current path
            if args[0] == '..':
                # Go to parent directory
                curr = pathlib.Path(curr).parent
            else:
                if not curr:
                    curr = pathlib.Path(args[0])
                else:
                    # Append path
                    new_path = curr.joinpath(args[0])
                    fs[curr].append(new_path)
                    curr = new_path
    for p in fs.keys():
        fs[p] = calculate_size(fs, p)
        if fs[p] <= 100000:
            ans1 += fs[p]
    print("Part 1: ", ans1)
    cli.submit_answer(1, ans1)
