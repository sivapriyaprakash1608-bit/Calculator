# Calculator using Functions
# The user chooses an operator and two numbers, and the program shows the result.
# It keeps running until the user types 'q'.


# Each operation has its own small function.
# A function only calculates and returns the answer; it does not ask or print.

def add(a, b):
  return a + b


def sub(a, b):
  return a - b


def mul(a, b):
  return a * b


def div(a, b):
  # Dividing by zero would crash Python, so check the second number first
  if b == 0:
    return "Cannot divide by Zero"
  return a / b


# The main function: asks the user, calls the right function, shows the result
def Calculator():

  # Keep running until the user chooses to quit
  while True:

    # Ask for the operator first, so the user can quit without typing numbers
    operator = input("Select your operator: +, -, *, / or Type 'q' if u want to quit: ")

    # If the user typed q, print a message and leave the loop
    if operator == "q":
      print("Exit")
      break

    # Handle wrong input (like letters) without crashing
    try:
      a = float(input("Enter your first no: "))   # float allows decimals like 2.5
      b = float(input("Enter your second no: "))
    except ValueError:
      # The user typed something that is not a number
      print("Thats not a no, try again")
      continue  # go back to the top and ask for the operator again

    # Choose the right function for the operator and print its answer
    if operator == "+":
      print(add(a, b))
    elif operator == "-":
      print(sub(a, b))
    elif operator == "*":
      print(mul(a, b))
    elif operator == "/":
      print(div(a, b))
    else:
      # The operator was not one of the four valid ones
      print("Invalid Operator")


# Start the program
Calculator()
