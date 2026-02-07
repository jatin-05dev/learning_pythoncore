# pattern no1 
# n=int(input("enter a number : "))
# for  i in  range(1,n+1):
#     for i in range(1,n+1):
#         print(i,end=" ")
#     print()
# pattern no 2

# n=int(input("enter a number : "))
# for  o in  range(1,n+1):
#     for i in range(1,o+1):
#         print(i,end=" ")
#     print()

# pattern no 3

# n=int(input("enter a number : "))
# x=1
# for  i in  range(1,n+1):
#     for _ in range(1,i+1):
#         print(x,end=" ")
#         x=x+1

#     print()

# pattern no 4


# n=int(input("enter a number : "))
# x=1
# for  i in  range(1,n+1):
#     for _ in range(1,i+1):
#         print(x,end=" ")
#         x=x+2

#     print()
# pattern no 4


# n=int(input("enter a number : "))
# x=2
# for  i in  range(1,n+1):
#     for _ in range(1,i+1):
#         print(x,end=" ")
#         x=x+2

#     print()
# pattern 5
# n=int(input("enter a number : "))
# for  i in  range(1,n+1):
#     for o in range(1,i+1):
#         print(2*o,end=" ") 
#     print()

# pattermn 6

# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     
#     print(" " * (n - i), end=" ")  
#     # print numbers in each row
#     for j in range(1, i+1):
#         print(j, end=" ")  
#     print() 

# pattern 7

# n = int(input("Enter number of rows: "))

# for i in range(1, n+1):
#     # print spaces before numbers for centering
#     print(" " * (n - i), end=" ")  
#     # print numbers in each row
#     for j in range(1, i+1):
#         print(j*2-1, end=" ") 
#     print()  # move to next line


# pattern 8
# n=int(input("enter number you want : "))
# for i in range(1,n+1):
#     ch="A"
#     for _ in range(1,n+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     print() 
# pattern 9

# n=int(input("enter number you want : "))
# ch="A"
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+1)
#     print() 


# patter 10

# n=int(input("enter number you want : "))
# ch="A"
# for i in range(1,n+1):
#     for _ in range(1,i+1):
#         print(ch,end=" ")
#         ch=chr(ord(ch)+2)
#     print() 


# pattern 11

# n = int(input("Enter number of rows: "))
# ch="A"
# for i in range(1, n+1):
#     print(" " * (n - i), end=" ")  
#     for j in range(1, i+1):
#         print(ch, end=" ")
#         ch=chr(ord(ch)+1) 
#     print()  

# pattern 12


# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     ch="A"
#     print(" " * (n - i), end=" ")  
#     for j in range(1, i+1):
#         print(ch, end=" ")
#         ch=chr(ord(ch)+1) 
#     print()  


# pattern 13

# n = int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     ch="A"
#     print(" " * (n - i), end=" ")  
#     for j in range(1, i+1):
#         print(ch, end=" ")
#         ch=chr(ord(ch)+2) 
#     print()  

# pattern 14

# n = int(input("Enter number of rows: "))
# i=1
# while(i<=n):
#     print("*"*i)
#     i=i+1
    

# pattern 15


# n = int(input("Enter number of rows: "))
# i=1
# while(i<=n):
#     print(" "*(n-i)+i*"*")
#     i=i+1
# pattern 16


# n = int(input("Enter number of rows: "))
# i=1
# while(i<=n):
#     print(" "*(n-i)+i*"* ")
#     i=i+1
    
# pattern 17

# n = int(input("Enter number of rows: "))
# i=1
# while(i<=n):
#     print(" "*(n-i)+i*"* ")
#     i=i+1


# # pattern 18
# n = int(input("Enter number of rows for pattern 18: "))
# i = n
# while i >= 1:
#     print("* " * i)
#     i = i - 1
# print()

# # pattern 19
# n = int(input("Enter number of rows for pattern 19: "))
# i = n
# while i >= 1:
#     print("* " * i)
#     i = i - 1
# print()

# # pattern 20
# n = int(input("Enter number of rows for pattern 20: "))
# i = n
# while i >= 1:
#     print("* " * i)
#     i = i - 1
# print()

# # pwttern 21
# n = int(input("Enter number of rows for pattern 21: "))
# i = 1
# while i <= n:
#     print("* " * i)
#     i = i + 1
# i = n - 1
# while i >= 1:
#     print("* " * i)
#     i = i - 1
# print()

# # paetr22
# n = int(input("Enter number of rows for pattern 22: "))
# i = 1
# while i <= n:
#     print("* " * i)
#     i = i + 1
# i = n - 1
# while i >= 1:
#     print("* " * i)
#     i = i - 1
# print()

# # patten 23
# n = int(input("Enter number of rows for pattern 23: "))
# i = 1
# while i <= n:
#     print("* " * i)
#     i = i + 1
# i = n - 1
# while i >= 1:
#     print("* " * i)
#     i = i - 1
# print()

# # patrern 24

# n = int(input("Enter number of rows for pattern 24: "))
# i = n
# while i >= 1:
#     print("* " * i)
#     i = i - 1
# i = 2
# while i <= n:
#     print("* " * i)
#     i = i + 1
# print()
 

# # patrern 25
# n = int(input("Enter number of rows for pattern 25: "))
# i = n
# while i >= 1:
#     print("* " * i)
#     i = i - 1
# i = 2
# while i <= n:
#     print("* " * i)
#     i = i + 1
# print()


# class Car:
#     def __init__(self,model,company):
#         self.model=model
#         self.company=company
#     def __str__(self):
#         return f"{self.model} and {self.company}"
    
# obj=Car("BMW","l")
# print(obj)



class counter:
    c=0
    def add(self):
        self.c=self.c+1
    def min(self):
        self.c=self.c-1
    
obj=counter()
obj.add()
print(obj.c)
obj.add()
print(obj.c)



