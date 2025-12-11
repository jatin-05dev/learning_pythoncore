# python_core_functions_demo.py

## 1. Basic Function Definition and Execution (Question 7 & 6)
# Demonstrates function definition, docstrings, positional, and keyword arguments.
print("--- 1. Function Definition and Arguments ---")

def calculate_area(length, width):
    """
    Calculates the area of a rectangle.

    :param length: The length of the rectangle (float or int).
    :param width: The width of the rectangle (float or int).
    :return: The area of the rectangle (float or int).
    """
    area = length * width
    return area

# Function call with positional arguments
area1 = calculate_area(10, 5)
# Function call with keyword arguments
area2 = calculate_area(width=7, length=12)

print(f"Area 1 (10x5): {area1}")
print(f"Area 2 (12x7): {area2}")
print("-" * 40)


## 2. Anonymous Functions (`lambda`) with `map()` and `filter()` (Questions 2 & 3)
# Demonstrates functional tools for processing iterables.
print("--- 2. map(), filter(), and lambda ---")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original numbers: {numbers}")

# Using map() to square every element
squared_numbers = list(map(lambda x: x**2, numbers))
print(f"Squared numbers (using map): {squared_numbers}")

# Using filter() to get only the even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers (using filter): {even_numbers}")
print("-" * 40)


## 3. Variable-Length Arguments (`*args` and `**kwargs`) (Questions 4 & 5)
# Demonstrates how to handle an arbitrary number of inputs.
print("--- 3. *args and **kwargs ---")

def process_data(required_value, *args, **kwargs):
    """Handles required, positional, and keyword arguments."""
    print(f"Required Value: {required_value}")
    print(f"Positional Arguments (*args): {args}")
    print(f"Keyword Arguments (**kwargs): {kwargs}")

# Example call
process_data(
    "Report_B",
    100, 200, "extra_note",
    status="Processed",
    environment="Production"
)
print("-" * 40)


## 4. Recursive Function for Factorial (Question 9)
# Demonstrates a function calling itself to solve a problem.
print("--- 4. Recursive Function (Factorial) ---")

def factorial(n):
    """Calculates the factorial of a non-negative integer n."""
    if n < 0:
        return "Factorial not defined for negative numbers"
    if n == 0:
        # Base case
        return 1
    else:
        # Recursive case
        return n * factorial(n - 1)

number_to_calculate = 6
result = factorial(number_to_calculate)
print(f"The factorial of {number_to_calculate} is: {result}") # Output: 720
print("-" * 40)