#10-1
from pathlib import Path
L_py = Path("learningPython.txt")
L_python = L_py.read_text()
print(L_python)

print("\n")

test = L_python.splitlines()
for letter in test:
    print(letter)

#10-4
path = Path("guest.txt")
name = input("What is your name? \n:")
path.write_text(name.title())