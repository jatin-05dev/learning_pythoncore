# -------------------------------------
# PYTHON FILE: ARRAY DSA QUESTIONS
# -------------------------------------

print("\n1. REVERSE AN ARRAY")
arr = [1, 2, 3, 4, 5]
print("Original:", arr)
reversed_arr = arr[::-1]
print("Reversed:", reversed_arr)

print("\n2. FIND MAXIMUM AND MINIMUM")
arr = [4, 7, 1, 9, 0]
print("Array:", arr)
print("Maximum:", max(arr))
print("Minimum:", min(arr))

print("\n3. MOVE ALL ZEROS TO END")
arr = [0, 1, 0, 3, 12]
print("Original:", arr)
result = [x for x in arr if x != 0]
zeros = [0] * arr.count(0)
arr = result + zeros
print("After moving zeros:", arr)

print("\n4. FIND MISSING NUMBER (1 TO N)")
arr = [1, 2, 4, 5, 6]
n = 6
missing = n*(n+1)//2 - sum(arr)
print("Array:", arr)
print("Missing number:", missing)

print("\n5. FIND MAJORITY ELEMENT")
arr = [2, 2, 1, 1, 2]
from collections import Counter
count = Counter(arr)
majority = max(count, key=count.get)
print("Array:", arr)
print("Majority element:", majority)

print("\n6. MAXIMUM SUBARRAY SUM (KADANE'S ALGORITHM)")
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum = curr_sum = arr[0]
for i in arr[1:]:
    curr_sum = max(i, curr_sum + i)
    max_sum = max(max_sum, curr_sum)
print("Array:", arr)
print("Maximum subarray sum:", max_sum)

print("\n7. TWO SUM PROBLEM")
arr = [2, 7, 11, 15]
target = 9
found = False
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            print(f"Pair with sum {target}: ({arr[i]}, {arr[j]})")
            found = True
            break
    if found:
        break

print("\n8. REMOVE DUPLICATES FROM SORTED ARRAY")
arr = [1, 1, 2, 2, 3, 4]
unique = []
for num in arr:
    if num not in unique:
        unique.append(num)
print("Original:", [1, 1, 2, 2, 3, 4])
print("After removing duplicates:", unique)

print("\n9. ROTATE ARRAY BY K STEPS")
arr = [1, 2, 3, 4, 5]
k = 2
rotated = arr[-k:] + arr[:-k]
print("Original:", arr)
print(f"Array rotated by {k} steps:", rotated)

print("\n10. SUBARRAY SUM EQUALS K")
arr = [1, 2, 3, 4, 5]
k = 9
found = False
for i in range(len(arr)):
    sum_sub = 0
    for j in range(i, len(arr)):
        sum_sub += arr[j]
        if sum_sub == k:
            print(f"Subarray with sum {k}:", arr[i:j+1])
            found = True
            break
    if found:
        break
