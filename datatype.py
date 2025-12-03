# -------------------------------
# 1. int
# -------------------------------
a = 10
b = -5
print(a, type(a))
print(b, type(b))

# -------------------------------
# 2. float
# -------------------------------
x = 10.5
y = -2.3
print(x, type(x))
print(y, type(y))

# -------------------------------
# 3. complex
# -------------------------------
z = 2 + 3j
print(z, type(z))
print(z.real)
print(z.imag)

# -------------------------------
# 4. bool
# -------------------------------
flag1 = True
flag2 = False
print(flag1, type(flag1))
print(flag2, type(flag2))

# -------------------------------
# 5. str
# -------------------------------
name = "Sumit"
print(name, type(name))
print(name[0])
print(name[1:4])

# -------------------------------
# 6. list
# -------------------------------
nums = [1, 2, 3, 4]
nums.append(5)
nums[0] = 10
print(nums, type(nums))

# -------------------------------
# 7. tuple
# -------------------------------
t = (1, 2, 3)
print(t, type(t))

# -------------------------------
# 8. dict
# -------------------------------
student = {"name": "Sumit", "age": 20}
print(student, type(student))
print(student["name"])
student["age"] = 21

# -------------------------------
# 9. set
# -------------------------------
s = {1, 2, 3, 3, 4}
print(s, type(s))
s.add(5)

# -------------------------------
# 10. frozenset
# -------------------------------
fs = frozenset([1, 2, 3, 4])
print(fs, type(fs))

# -------------------------------
# 11. bytes
# -------------------------------
bts = bytes([65, 66, 67])
print(bts, type(bts))

# -------------------------------
# 12. bytearray
# -------------------------------
ba = bytearray([65, 66, 67])
ba[0] = 68
print(ba, type(ba))

# -------------------------------
# 13. memoryview
# -------------------------------
data = bytearray(b"hello")
m = memoryview(data)
print(m[0])

# -------------------------------
# 14. range
# -------------------------------
r = range(1, 6)
print(list(r))
print(type(r))

# -------------------------------
# 15. NoneType
# -------------------------------
x_none = None
print(x_none, type(x_none))
