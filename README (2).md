# Calculator

A command-line calculator written in Python using functions. The user picks an operator and two numbers, and the program prints the result. It keeps running until the user quits.

## Features

- Addition, subtraction, multiplication and division
- Works with decimal numbers (for example `2.5`)
- Shows "Cannot divide by Zero" instead of crashing
- Handles wrong number input (letters, blank) with a clear message
- Rejects invalid operators
- Type `q` to quit

## Concepts Used

- Functions with parameters and `return`
- Difference between `return` and `print`
- `while True` loop with `break` and `continue`
- `try / except ValueError` for error handling
- `if / elif / else`
- Type conversion with `float()`

## How to Run

1. Install [Python 3](https://www.python.org/downloads/)
2. Download `calculator.py`
3. Open a terminal in the file's folder and run:

```
python calculator.py
```

## Sample Output

```
Select your operator: +, -, *, / or Type 'q' if u want to quit: +
Enter your first no: 5
Enter your second no: 3
8.0
Select your operator: +, -, *, / or Type 'q' if u want to quit: /
Enter your first no: 10
Enter your second no: 0
Cannot divide by Zero
Select your operator: +, -, *, / or Type 'q' if u want to quit: q
Exit
```

## Possible Improvements

- Reject an invalid operator before asking for the numbers
- Add `%` (remainder) and `+/-` (change sign)
- Keep the last result as the first number of the next calculation
- Rebuild it using a `Calculator` class (OOP)
- Build a graphical version with `tkinter`

## Author

Your Name
