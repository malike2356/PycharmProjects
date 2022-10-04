from pathlib import Path

path = Path()
for file in path.glob("*.py"):  # find all files ending with .py
    print(file)
