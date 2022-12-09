import argparse
import datetime
import os

from aocclient.client import Client

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Run me to get started with Advent of Code",
        epilog="Happy coding!")
    parser.add_argument("-y", "--year", action="store", default=datetime.date.today().year,
                        type=int, help="Year, it's year, by default use the current year")
    parser.add_argument("-d", "--day", action="store", default=1,
                        type=int, help="The challenge day, by default start from day 1")
    args = parser.parse_args()
    print(args)

    # Create directory
    daydir = os.path.join(str(args.year), f'day{args.day:02d}')
    if not os.path.isdir(daydir):
        os.mkdir(daydir, mode=0o755)

    # Set the current working directory
    os.chdir(daydir)

    # Create file
    template = """import os

from aocclient.client import Client

cli = Client(year={}, day={})

ans1 = None
ans2 = None

with open(os.path.join(os.getcwd(), "input.txt")) as f:
    pass
"""
    with open(f'day{args.day:02d}.py', 'w') as f:
        f.write(template.format(args.year, args.day))

    # Create link
    os.symlink('../../aocclient', 'aocclient')

    # Setup
    cli = Client(year=args.year, day=args.day)
    cli.setup()
