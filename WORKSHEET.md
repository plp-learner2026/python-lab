# Python Project Setup, Git, and GitHub Workflow — Worksheet

## Part A — Project Setup

Commands used:
- mkdir python_lab, mkdir src tests docs — created folders
- touch src/main.py src/utils.py src/config.py — created empty Python files
- echo "My Python Lab Project" > docs/README.md — wrote text using output redirection

Why separate src, tests, docs:
Separating code by purpose keeps a project organized and predictable as it grows. Source code stays in src, tests in tests, and documentation in docs, so anyone working on the project knows exactly where to look. It also makes it easy to exclude certain folders from packaging, and builds good habits early even on small projects.

## Part B — Git Init and First Commit

What .gitignore does:
.gitignore tells Git which files and folders to never track. _pycache_/ and *.pyc are ignored because they are automatically generated compiled Python files recreated every time code runs. .env is ignored because it usually holds secrets like passwords or API keys that should never be uploaded to a public repository.

What commit history reveals:
git log shows every commit with its author, date, and message, creating a timeline of a project's development that helps track progress and debug issues over time.

## Part C — Python Code

utils.py:

def square(n):
    return n ** 2

def is_even(n):
    return n % 2 == 0

def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def greet(name):
    return f"Hello, {name}! Welcome to the Python Lab."

main.py:

from utils import square, is_even, celsius_to_fahrenheit, greet

number = float(input("Enter a number: "))

print(f"Square: {square(number)}")

if is_even(number):
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(number)}")

name = input("Enter your name: ")
print(greet(name))

How Python's import system connects main.py to utils.py:
The import line tells Python to open utils.py in the same folder and bring specific function names into main.py's namespace, allowing main.py to call square(number) directly instead of utils.square(number).

Sample test outputs (3 different inputs):

Input: 4
Square: 16.0
4.0 is even
Fahrenheit equivalent: 39.2

Input: 7
Square: 49.0
7.0 is odd
Fahrenheit equivalent: 44.6

Input: -3
Square: 9.0
-3.0 is odd
Fahrenheit equivalent: 26.6

## Part D — GitHub and Branch Workflow

Why developers use branches and pull requests instead of committing directly to main:
Branches let developers build and test new features in isolation without risking the stable code on main. A pull request is a formal request to merge those changes, giving a clear record of what changed and why.

What happens during code review on a pull request:
Other developers read through the proposed changes, leave comments, suggest edits, and approve or request changes before anything is merged, catching bugs or issues early.
