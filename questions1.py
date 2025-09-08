'''
-- Topics covered

variables, datatypes, operators, strings, lists, dictionaries, tuples, sets, input/output

-- Easy

Write a Python program that takes an integer input from the user and prints whether it is even or odd.
Create a list of numbers from 1 to 10, reverse it, and print the reversed list.
Write a program to replace all occurrences of "hello" with "hi" in the string "hello world, hello Python".

-- Medium

Create a dictionary where the keys are strings "a", "b", "c" and the values are lists of numbers. Print the second element from the list of key "a".
Write a program to count how many times the number 5 appears in the tuple (1, 5, 2, 5, 3, 5, 4).
Given a list of integers, remove duplicates using a set, then convert it back into a sorted list.

-- Hard

Take a string input from the user. Count how many vowels are in the string, and store the counts in a dictionary (e.g., {'a': 2, 'e': 1}).
Write a program that takes a nested list (matrix) and prints the transpose. Example: [[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]].
Given two lists of numbers, return a set containing numbers that are in first list but not in second, and another set containing numbers that are common in both.
'''

############# SOLUTIONS ########################

'''
-- Easy

1 - Write a Python program that takes an integer input from the user and prints whether it is even or odd.

  num = int(input("Enter the number to check if it's even or odd: "))
  if num < 0:
    print("Error! Enter a valid number >=0")
  elif num % 2 == 0:
    print(f"The entered number {num} is even number")
  else:
    print(f"The entered number {num} is odd number")

2 - Create a list of numbers from 1 to 10, reverse it, and print the reversed list.

  nums = []
  for i in range(1,11):
    nums.append(i)

  print(f"The list of numbers before reversed: {nums}")
  nums_reversed = nums[::-1]
  print(f"The list of numbers after reversed: {nums_reversed}")

3 - Write a program to replace all occurrences of "hello" with "hi" in the string "hello world, hello Python".

  sentence = "hello world, hello Python"
  print(sentence.replace("hello", "hi"))

-- Medium

4 - Create a dictionary where the keys are strings "a", "b", "c" and the values are lists of numbers. Print the second element from the list of key "a".

  dict_values = {
    'a': [1,2,3],
    'b': [4,5,6],
    'c': [7,8,9]
  }
  print(dict_values['a'][1])

5 - Write a program to count how many times the number 5 appears in the tuple (1, 5, 2, 5, 3, 5, 4).

  num_tuple = (1, 5, 2, 5, 3, 5, 4)
  print(f"Number of times 5 appeared is: {num_tuple.count(5)}")

6 - Given a list of integers, remove duplicates using a set, then convert it back into a sorted list.

  unsorted_list_numbers = [1,4,6,3,1,2,4,7,8,9,5,6,8]
  sorted_undup_set_numbers = sorted(set(unsorted_list_numbers))
  print(f"The sorted and duplicates removed list in format is: {sorted_undup_set_numbers}")

-- Hard

7 - Take a string input from the user. Count how many vowels are in the string, and store the counts in a dictionary (e.g., {'a': 2, 'e': 1}).

user_input = input("Enter a string: ")
vowels = 'aeiouAEIOU'
result = {}
for char in user_input:
  if char in vowels:
    result[char] = result.get(char, 0) + 1

print(f"The final updated dictionary is: {result}")

8 - Write a program that takes a nested list (matrix) and prints the transpose. Example: [[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]].

  nested_list = [[1,2,3],[4,5,6]]
  result = []

  for value in range(0, len(nested_list[0])):
      temp = []
      for row in nested_list:
          temp.append(row[value])
      result.append(temp)

  print(f"The final pair of the given nested list is: {result}")

9 - Given two lists of numbers, return a set containing numbers that are in first list but not in second, and another set containing numbers that are common in both.

  list1 = {1,2,3,4,5}
  list2 = {4,5,6,7,8,9}

  contains_in_list1 = set(list1.difference(list2))
  common_in_both_list = set(list1.intersection(list2))
  print(contains_in_list1)
  print(common_in_both_list)

'''