# bubble sort 

# def sor(l):
#  n=len(l)
#  for i in range(n-1):
#     iss=False
#     for j in range(n-i-1):
#         if l[j]>l[j+1]:
#             l[j],l[j+1]=l[j+1],l[j]
#             iss=True
#     if (not iss):
#      break
#  return l
# l=[2,5,8,4,8,2,5]
# print(sor(l))

# selection sort

# def sor(l):
#  n=len(l)
#  for i in range(n-1):
#     smi=i
#     for j in range(i+1,n):
#         if l[j]<l[smi]:
#            smi=j

#     l[i],l[smi]=l[smi],l[i]        
#  return l
# l=[2,5,8,4,8,2,5]
# print(sor(l))

 # insertion sort

# def sor(l):
#  n=len(l)
#  for i in range(n):
#     curr=l[i]
#     pr=i-1
#     while pr>=0 and l[pr]>curr:
#        l[pr+1]=l[pr]
#        pr=pr-1
#     l[pr+1]=curr 

#  return l

# l=[2,5,8,4,8,2,5]
# print(sor(l))

# merge sort 
# def merge(l, st, mid, end):
#     temp = []
#     i = st
#     j = mid + 1
#     while i <= mid and j <= end:
#         if l[i] <= l[j]:
#             temp.append(l[i])
#             i += 1
#         else:
#             temp.append(l[j])
#             j += 1
#     while i <= mid:
#         temp.append(l[i])
#         i += 1
#     while j <= end:
#         temp.append(l[j])
#         j += 1
#     for k in range(len(temp)):
#         l[st + k] = temp[k]
# def mergesort(l, st, end):
#     if st < end:
#         mid = (st + end) // 2
#         mergesort(l, st, mid)
#         mergesort(l, mid + 1, end)
#         merge(l, st, mid, end)
# l = [98, 8, 4, 56, 2, 3]
# mergesort(l, 0, len(l) - 1)
# for i in l:
#     print(i)

# quck sort
def par(l, st, end):
    idx = st - 1
    pi = l[end]

    for j in range(st, end):
        if l[j] <= pi:
            idx += 1
            l[j], l[idx] = l[idx], l[j]

    idx += 1
    l[end], l[idx] = l[idx], l[end]
    return idx


def qsort(l, st, end):
    if st < end:
        pid = par(l, st, end)
        qsort(l, st, pid - 1)
        qsort(l, pid + 1, end)
    return l


l = [98, 8, 4, 56, 2, 3]
print(qsort(l, 0, len(l) - 1))



