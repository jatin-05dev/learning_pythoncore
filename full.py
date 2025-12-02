# ============================================
#            CORE PYTHON FULL CODE
#        (Basics → Loops → Functions → OOP)
# ============================================


# ---------------------
# 1. BASIC PYTHON
# ---------------------

# Variables
name = "Jatin"
age = 21
is_student = True

print("\n--- BASIC PYTHON ---")
print("Name:", name)
print("Age:", age)
print("Is Student:", is_student)

# Data Types
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of is_student:", type(is_student))


# ---------------------
# 2. LOOPS
# ---------------------
print("\n--- LOOPS ---")

# For Loop
for i in range(1, 6):
    print("For Loop Number:", i)

# While Loop
count = 5
while count > 0:
    print("While Loop Countdown:", count)
    count -= 1


# ---------------------
# 3. FUNCTIONS
# ---------------------
print("\n--- FUNCTIONS ---")

def greet(user):
    return f"Hello, {user}! Welcome to Python."

print(greet("Jatin"))

def add(a, b):
    return a + b

print("10 + 20 =", add(10, 20))


# ---------------------
# 4. OOP (Classes & Objects)
# ---------------------
print("\n--- OOP ---")

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Student Name: {self.name}, Roll No: {self.roll}")

s1 = Student("Jatin", 101)
s1.show()


# ---------------------
# 5. FILE HANDLING
# ---------------------
print("\n--- FILE HANDLING ---")

# Writing to file
with open("data.txt", "w") as f:
    f.write("This is Python File Handling Example.")

# Reading file
with open("data.txt", "r") as f:
    print("File Content:", f.read())


# ---------------------
# END OF CORE PYTHON
# ---------------------
print("\n--- DONE ✔ ---")
