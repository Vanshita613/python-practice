#Q2.check even or odd number

# a=int(input("enter a nmber:"))

# if a%2==0:
#     print("number is even ")
# else:
#     print("number is odd!")




#Q3.Write a program to find the largest of three numbers.
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))

# if a>b and a>c:
#     print(a,"is the largest")
# elif( b>a and b>c):
#     print(b ,"is the largest")
# else:
#     print(c,"is the largest")



#Q4.Swap Two Numbers
#using temp variablwe
# a=int(input("enter a number:"))
# b=int(input("enter second number:"))
# temp=a
# a=b
# b=temp

# print("a=",a)
# print("b=",b)


# #without using temp variable
# a=int(input("enter first number:"))
# b=int(input("enter second number:"))

# a,b=b,a

# print("a=",a)
# print("b=",b)


#Q5.factorial
# n=int(input("entr a number:"))

# fact=1
# i=1

# while i<=n:
#     fact=fact*i
#     i+=1
# print(fact)


#Q6. prime number
# num=int(input("ente a numbr:"))

# if num<=1:
#     print("number is not a prome number")

# else:
#     for i in range (2,num):
#         if  num%i==0:
#             print(num,"is not a prime number!")
#             break 
#     else:
#         print(num,"is a prime number")
        

#Q7. Fibonacci series
# n=int(input("enter a number;"))

# a=0
# b=1

# for i in range(n):
#     print(a,end=" ")
    
#     c=a+b
#     a=b
#     b=c



#Q8. Reverse a number

# n = int(input("Enter a number: "))

# reverse = 0

# while n > 0:
#     digit = n % 10
#     reverse = reverse * 10 + digit
#     n = n // 10

# print("Reverse =", reverse)

#Q9
n = input("Enter a number: ")

if n == n[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
        
#36
year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")




#37
arr = list(map(int, input("Enter numbers: ").split()))

largest = float('-inf')
second = float('-inf')

for n in arr:
    if n > largest:
        second = largest
        largest = n
    elif n > second and n != largest:
        second = n

print("Second largest =", second)


#40
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not Anagrams")


#44
arr = [10, 20, 30, 40, 50]

key = int(input("Enter element: "))

low = 0
high = len(arr) - 1

found = False

while low <= high:

    mid = (low + high) // 2
