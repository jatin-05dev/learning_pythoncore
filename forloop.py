
l=[1,2,3,4,5,6,78]
l1=[]
for i in l:
    if(i%2==0):
       l1.append(i)

print(l1)

# odd ki
list
l=[1,2,3,4,5,6,78]
l1=[]
for i in l:
    if(i%2!=0):
       l1.append(i)

print(l1)


# tuple
l=[1,2,3,4,5,6,78]
l1=[]
for i in l:
    if(i%2!=0):
       l1.append(i)

print(tuple(l1)) 

dict

d={'name':'jatin','age':5,'active':True}
for i in d.keys():
    print(i)
for i in d.values(),d.keys():
    print(i)
print(d.items())
# dic se ati he to do rkh 
for i,k in d.items():
    print(i,"=",k)

for i,k in d.items():
    print(i,k)

# parten

# simple
for i in range(1,6):
    print(i,end=" ")

n=int(input("enter number: "))
for i in range(1,n+1):
    for i in range(1,n+1):
        print(i,end=" ")
    print()
# pattern

n=int(input("enter ani"))
for l in range(1,n+1):
    for i in range(1,l+1):
        print(i*2-1,end=" ")
    print()

# odd even
n=int(input("enter number: "))
for j in range(1,n+1):
    for i in range(1,j+1):
        print(i*2-1,end=" ")
    print()

x=1
for i in range(1,n+1):
    for  j in range(1,i+1):
        print(x,end=",")
        x=x+2
    print()
 

# patrern 
n=int(input("enyter a number : "))
x=1
for i in range(1,n+1):
    for _ in range(1,i+1):
        print(x,end=" ")
        x=x+2
    print()

# alpha key
x="k" 
y=chr(ord(x)+1)
print(y)
n=int(input("enter char"))
for i in range(1,n+1):
    ch='a'
    for _ in range(1,i+1):
        print(ch,end=' ')
        ch=chr(ord(ch)+1)
    print()
# nesxrt

for i in range(1,n+1):
    ch="a"
    for _ in range(1,n+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
n=int(input("enter char"))
for i in range(1,n+1):
    ch='a'
    for _ in range(1,i+1):
        print(ch,end=' ')
        ch=chr(ord(ch)+2)
    print()
