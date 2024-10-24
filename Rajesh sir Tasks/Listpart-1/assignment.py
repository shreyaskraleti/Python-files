# 1. Given a list of strings representing the days of the week, write a function that returns 
# a sublist containing only the weekdays (Monday to Friday).
l1 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
def week_days(list1):
    return list1[0:5]
print(week_days(l1))

# 2. Write a program that inserts a specific value at the third position of a list of integers 
# and then removes the last element from the list.
def insert_remove(list1):
    list1.insert(2,25)
    list1.pop()
    return list1
list1 = [1,2,3,4,5,6,7,8,9,10]
print(insert_remove(list1))

# 3. Given a list of unsorted integers, write a function that returns the list sorted in ascending order. 
# Next, sort the list in descending order and return it.
def sort(list1):
    list1.sort()
    return list1
def sort_desc(list1):
    list1.sort(reverse=True)
    return list1
list1 = [2,1,3,6,4,7,5,9,8,10]
print(sort(list1))
print(sort_desc(list1))

# 4. Create a function that reverses a list of words. Test the function with a list of five random words. 
def reverse_word(list1):
    list1.reverse()
    return list1
list1 = ["guava", "banana", "apple", "cherry", "orange"]
print(reverse_word(list1))

# 5. Write a function that counts how many times a specific element appears in a list. 
# The function should also return the index of the first occurrence of that element. 
def count_index(list1, element):
    count = list1.count(element)  # Count how many times the element appears in the list
    if count > 0:      # Find the index of the first occurrence of the element
        first_index = list1.index(element) 
    else:  # If the element is not found, return -1
        first_index = -1
    return count, first_index
list1 = [1,2,3,2,4,3,5,6,7]
print(count_index(list1,2))
print(count_index(list1, 5))
print(count_index(list1,10))
        
# 6. Given a list of ages, write a function that returns a new list containing 
# only the ages that are greater than 18.
def age(list1):
    return [age for age in list1 if age > 18] # use list comprehension
list1 = [10,12,15,20,19,30]
print(age(list1))

# 7. Write a function that removes all duplicate elements from a list of integers and 
# returns the list with only unique elements.
def remove_duplicates(list1):
    return list(set(list1))
list1 = [1,2,1,2,3,4,3,5,4,6,7]
print(remove_duplicates(list1))

# 8. Given a list of fruit names, write a function that checks if a specific fruit is in the list.
# The function should return True if the fruit is present, otherwise False. 
def check_fruit(list1, fruit):
    return fruit in list1
list1 = ["apple", "banana", "cherry", "date", "orange"]
print(check_fruit(list1, "banana"))
print(check_fruit(list1, "grapes"))

# 9. Create two lists of the same length. Write a function that combines these two lists into a list of tuples, 
# where each tuple contains elements from the corresponding positions in the original lists. 
"""zip(): This function pairs elements from both lists based on their positions. 
It creates an iterator of tuples, where each tuple contains one element from each list.
list(): The zip() function returns an iterator, so we convert it into a list to get the final output."""

def combine(list1, list2):
    return list(zip(list1, list2)) # Use the zip() function to combine elements from both lists
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
print(combine(list1, list2))

# 10.Write a function that splits a list into two separate lists: one containing 
# all the positive numbers and the other containing all the negative numbers.
def split_list(numbers):
    positive_numbers = [num for num in numbers if num>0]
    negative_numbers = [num for num in numbers if num<0]
    return positive_numbers, negative_numbers
numbers = [1,2,3,4,5,-1,-2,-3,-4,-5]
positive_numbers,negative_numbers = split_list(numbers)
print("positive numbers are: ", positive_numbers)
print("negative numbers are: ", negative_numbers)
