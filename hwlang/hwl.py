import sys
from split_commands import split_comands
from run_commands import run

if len(sys.argv) < 2:
    print("Usage: python hwl.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

# Пример использования:
commands = split_comands(file_path)
run(commands)