 # using the calculater functions from the calculater.py file,
 # Create a main calculater function that uses if/else logic to
 # allow the user to select differnet arthemetic operations and
 # then perform those operations by running their perspective function.

 # Example: an input where if the user enter 1, it will run the addition function.
 # 1= addition()
 # 2= subtraction()
 # 3= multiply()
 # 4= division ()


def addition(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtraction(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def division(a, b):
    """Return the quotient of two numbers. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

    from calculator import addition, subtraction, multiply, division

def main_calculator():
    print("=== Simple Calculator ===")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

   






