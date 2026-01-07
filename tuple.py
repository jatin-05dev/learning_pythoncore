"""
PYTHON TUPLE – ALL IN ONE (ONLY CODE)
"""

# 1️⃣ Tuple creation
t1 = (1, 2, 3)
t2 = 1, 2, 3          # packing
t3 = (5,)             # single element tuple

print(t1, t2, t3)

# 2️⃣ Indexing & slicing
t = (10, 20, 30, 40)
print(t[0])
print(t[-1])
print(t[1:3])

# 3️⃣ Immutable proof
try:
    t[0] = 100
except TypeError as e:
    print("Immutable:", e)

# 4️⃣ Tuple functions
t = (10, 20, 20, 30)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(t.count(20))
print(t.index(30))

# 5️⃣ Looping
for x in t:
    print(x)

# 6️⃣ Unpacking
t = (1, 2, 3)
a, b, c = t
print(a, b, c)

# Extended unpacking
t = (1, 2, 3, 4, 5)
a, *b, c = t
print(a, b, c)

# 7️⃣ Nested tuple
t = (1, (2, 3), (4, 5))
print(t[1][1])

# 8️⃣ Mutable object inside tuple
t = (1, 2, [3, 4])
t[2][0] = 100
print(t)

# 9️⃣ Tuple vs List
lst = [1, 2, 3]
tpl = (1, 2, 3)
print(lst, tpl)

# 🔟 Convert tuple to list & back
t = (1, 2, 3)
l = list(t)
l[0] = 99
t = tuple(l)
print(t)

# 1️⃣1️⃣ Coding practice
# Even elements
t = (1, 2, 3, 4, 5, 6)
for x in t:
    if x % 2 == 0:
        print("Even:", x)

# Reverse tuple
t = (1, 2, 3)
print(t[::-1])

print("END")
