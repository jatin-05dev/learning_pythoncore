#  1. WAP to give list of all factors for any number.
n=int(input("Enter any no:"))
factors = []
for i in range(1,n+1):
 if n%i==0:
  factors.append(i)
print("Factors are :",factors)
# 2. WAP to arrenge all items from list in assending order.
l = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(l)
for i in range(n-1):
 for j in range(n-i-1):
  if l[j] > l[j+1]:
   l[j], l[j+1] = l[j+1], l[j]
print(l)
# 3. WAP to arrenge all items from list in desending order.
l = [64, 34, 25, 12, 22, 11, 90, 5]
n = len(l)
for i in range(n-1):
 for j in range(n-i-1):
  if l[j] < l[j+1]:
   l[j], l[j+1] = l[j+1], l[j]
print(l)
# 4. WAP to find maximum digit in given list.
l = [2,4,9,3,5]
max = l[0]
for i in range(len(l)-1):
 if l[i]>l[i+1]:
  max = l[i]
  l[i],l[i+1]=l[i+1],l[i]
else:
 max=l[i+1]
print(max)
# 5. WAP to find minimum digit in given list.

l = [2,4,9,3,5]
min = l[0]
for i in range(len(l)-1):
 if l[i]<l[i+1]:
  min = l[i]
 l[i],l[i+1]=l[i+1],l[i]
else:
 min=l[i+1]
print(min)
# 6. WAP to check given number is either perfect number or not.
n=int(input("Enter any no:"))
sum = 0
for i in range(1,n):
 if n%i==0:
  sum=sum+i
if n==sum:
 print(f'given number {n} is perfect number')
else:
 print(f'given number {n} is not a perfect number')
# 7. WAP to arrenge all even and odd no at a place.
# i/p :- [2,1,3,8,4,8,5]
# o/p :- [2,8,4,8,1,3,5]
l = [2,1,3,8,4,8,5]
l1=[]
for i in l:
 if i%2==0:
  l1.append(i)
for i in l:
  if i%2 !=0:
   l1.append(i)
print(l1)
# 8. WAP to arrenge all zeroes at the end.
# i/p :- [2,0,3,0,1,0,5]
# o/p :- [2,3,1,5,0,0,0]
l = [2,0,3,0,1,0,5] # [2,3,1,5,0,0,0]
l1=[]
for i in l:
 if i !=0:
  l1.append(i)

n = len(l)-len(l1)
for i in range(n):
 l1.append(0)
print(l1)
# 9. WAP to arrenge below menrtion format.
# i/p :- l = [1, 1, 1, 2, 3, 4, 3, 4, 2, 5, 6, 5, 7]
# o/p :- {1: 3, 2: 2, 3: 2, 4: 2, 5: 2, 6: 1, 7: 1}
l = [1, 1, 1, 2, 3, 4, 3, 4, 2, 5, 6, 5, 7]
output_dict = {}
for item in l:
 if item in output_dict:
  output_dict[item] += 1
else:
 output_dict[item] = 1
print(output_dict)
 