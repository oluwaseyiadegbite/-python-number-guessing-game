# Python Number Guessing Game

An interactive command-line game built with Python, featuring two ways to play: guess the computer’s secret number, or let the computer find yours using binary search.

## Game Modes

### 1. You Guess
The computer chooses a random number between 1 and 100. Enter your guesses and receive “Too high” or “Too low” hints until you find it. The game tracks how many guesses you take.

### 2. Computer Guesses
Think of a number between 1 and 100, and the computer will try to find it. Respond with:

- `h` — the computer’s guess is too high.
- `l` — the computer’s guess is too low.
- `c` — the computer’s guess is correct.

The computer uses binary search to narrow down the possible numbers after each response. With accurate feedback, it can find any number in this range in at most 7 guesses.

## Features

- Two interactive game modes.
- Random number generation using Python’s built-in `random` module.
- Binary search for efficient computer guessing.
- Guess counting in both modes.
- Error handling for non-integer player input.
- Validation of computer-mode feedback.
- A warning when feedback leaves no possible number.

## Technologies

- **Language:** Python 3
- **Interface:** Command line
- **Dependencies:** Python standard library only

## How to Run

1. Install Python 3.
2. Download `guessing_game.py` from this repository.
3. Open a terminal in the folder containing the file.
4. Run:

```bash
python3 guessing_game.py
```

On systems where Python 3 uses the `python` command, run:

```bash
python guessing_game.py
```

Choose `1` to guess the computer’s number or `2` to let the computer guess yours.

## Example Gameplay

```text
1 = You guess, 2 = Computer guesses: 1
Guess a number (1-100): 50
Too low
Guess a number (1-100): 75
Too high
Guess a number (1-100): 63
Correct! You took 3 guesses.
```

## How Binary Search Works

The computer starts with the full range of possible numbers and guesses the midpoint. Your feedback tells it which half to keep.

For example, if it guesses 50 and you answer “too low”, it searches between 51 and 100 next. This process repeats until your number is found.

For a range containing **n** numbers, binary search requires **O(log n)** guesses in the worst case, assuming accurate feedback.

## Skills Demonstrated

- Breaking a program into reusable functions.
- Using loops and conditional statements.
- Handling invalid input with `try` and `except`.
- Implementing a binary search algorithm.
- Managing user interaction through terminal input and output.
- Documenting functions with docstrings.

## Planned Improvements

- Reject player guesses outside the allowed range.
- Add difficulty levels and custom number ranges.
- Allow players to start another round without restarting the program.
- Keep prompting after an invalid menu selection.
- Add automated tests for game logic.
