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


# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Enter number of terms: "))

# for i in range(n):
#     print(fibonacci(i), end=" ")


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)

# num = int(input("Enter a number: "))

# print("Factorial:", factorial(num))


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(5))



# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")
# if sorted(s1) == sorted(s2):
#     print("Anagrams")
# else:
#     print("Not Anagrams")


# a = [1, 3, 5]
# b = [2, 4, 6]
# merged = sorted(a + b)
# print(merged)


# num = [1, 2, 3, 4, 5]
# k = 2
# k %= len(num)
# result = num[-k:] + num[:-k]
# print(result)



# sentence = input("Enter a sentence: ")

# words = sentence.split()

# longest = max(words, key=len)

# print("Longest Word:", longest)

#linear search
# numbers = [10, 20, 30, 40, 50]

# key = int(input("Enter number: "))

# if key in numbers:
#     print("Found")
# else:
#     print("Not Found")

# #binary search
# numbers = [10, 20, 30, 40, 50]

# key = int(input("Enter number: "))

# low = 0
# high = len(numbers) - 1

# found = False

# while low <= high:
#     mid = (low + high) // 2

#     if numbers[mid] == key:
#         found = True
#         break
#     elif numbers[mid] < key:
#         low = mid + 1
#     else:
#         high = mid - 1

# if found:
#     print("Found")
# else:
#     print("Not Found")




# s = input("Enter string: ")
# v = c = d = sp = 0
# for ch in s:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             v += 1
#         else:
#             c += 1
#     elif ch.isdigit():
#       d += 1
#     else:
#       sp += 1
# print("Vowels:", v)
# print("Consonants:", c)
# print("Digits:", d)
# print("Special:", sp)



# class Student:
#     def __init__(self):
#       self.students = {}
#     def add(self, roll, name):
#       self.students[roll] = name
#     def display(self):
#         print(self.students)
#     def search(self, roll):
#         print(self.students.get(roll, "Not Found"))
# s = Student()
# s.add(1, "Alice")
# s.add(2, "Bob")
# s.display()
# s.search(1)


# class Bank:
#     def __init__(self):
#         self.balance = 0

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient Balance")

#     def show(self):
#         print("Balance:", self.balance)

# obj = Bank()

# obj.deposit(1000)
# obj.withdraw(300)
# obj.show()


# file = open("sample.txt", "r")

# text = file.read()

# print("Lines:", len(text.splitlines()))
# print("Words:", len(text.split()))
# print("Characters:", len(text))

# file.close()



# source = open("sample.txt", "r")

# content = source.read()

# source.close()

# destination = open("copy.txt", "w")

# destination.write(content)

# destination.write("\nThis text is appended.")

# destination.close()

# print("File copied successfully.")


# library = {}
# def add_book(book):
#     library[book] = "Available"
# def issue_book(book):
#     if library.get(book) == "Available":
#         library[book] = "Issued"
# def return_book(book):
#     library[book] = "Available"
# add_book("Python")
# issue_book("Python")
# print(library)
# return_book("Python")
# print(library)


# while True:
#     print("\n1.Add 2.Subtract 3.Multiply")
#     print("4.Divide 5.Modulus 6.Power 7.Exit")

#     choice = int(input("Enter choice: "))
#     if choice == 7:
#         break
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
    
#     if choice == 1:
#         print(a + b)
#     elif choice == 2:
#         print(a - b)
#     elif choice == 3:
#         print(a * b)
#     elif choice == 4:
#         print(a / b)
#     elif choice == 5:
#         print(a % b)
#     elif choice == 6:
#         print(a ** b)
#     else:
#         print("Invalid Choice")

