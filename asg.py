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

numbers = [1, 2, 2, 3, 4, 4, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(result)