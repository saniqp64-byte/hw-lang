import re
import sys


def split_comands(file):
    commands = {}

    with open(file, "r") as file:
        try:
            for line in file.readlines():
                line = line.replace('&', '\n')
                mach = re.search(r"([^(]+)\(([^)]+)\)\s*(.*)", line)
                commands[mach.group(1)] = mach.group(2)

            file.close()
        except:
            print("you invalid")
            sys.exit()

    return commands
            