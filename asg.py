#Write a program to find the second largest element in a list.  


# numbers = [10, 20, 4, 45, 99]

# # Remove duplicates and sort the list
# unique_numbers = list(set(numbers))
# unique_numbers.sort()

# # Check if there are at least two unique elements
# if len(unique_numbers) >= 2:
#     print("Second largest element:", unique_numbers[-2])
# else:
#     print("No second largest element exists.")


#Write a program to check whether a given string is a palindrome


# text = input("Enter a string: ")

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# numbers = [1, 2, 2, 3, 4, 4, 5]

# result = []

# for num in numbers:
#     if num not in result:
#         result.append(num)

# print(result)

# Q1 


# numbers=[1,4,2,78,9,44]

# numbers.sort()

# print("second largest element is:",numbers[-2])

#Q2

# text = input("Enter a string: ")

# if (text == text[::-1]):
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#Q3

# text = input("Enter a string: ")

# freq = {}

# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# print(freq)

#q4

# list=[2,3,4,5,4,6,7,7]

# result=[]

# for num in list:
#     if num not in result:
#         result.append(num)
# print(result)


# text = input("Enter a string: ")

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


#Q5
# list1=[3,6,8,4,2,9,]
# list2=[5,4,3,2,7,0,9]

# common=[]

# for i in list1:
#     if i in list2:
#         common.append(i)
# print(common)



#Q6
# data = [(1, 3), (4, 1), (2, 5), (6, 2)]

# data.sort(key=lambda x:x[1])

# print(data)



# text=input("enter a string:")

# for ch in text:
#     if text.count(ch)==1:
#         print("first non-repeating character:",ch)
#         break


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

num = int(input("Enter a number: "))

print("Factorial:", factorial(num))


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))



s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")


a = [1, 3, 5]
b = [2, 4, 6]
merged = sorted(a + b)
print(merged)


num = [1, 2, 3, 4, 5]
k = 2
k %= len(num)
result = num[-k:] + num[:-k]
print(result)

