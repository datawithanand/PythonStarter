# EASY — check the basics (1–2 lines each)
'''
1. Write a program that reads an integer from `input()` and prints `"Even"` or `"Odd"`. Handle `0` and negative numbers correctly.

  num = int(input("Enter the number to check if it's even or odd: "))
  if num %2 == 0: # Handles all numbers including zero and negative numbers. No extra condition check required.
    print(f"The enter number {num} is even number.")
  else:
    print(f"The enter number {num} is odd number.")

2. Create a list of numbers from `1` to `10`, reverse it, and print the reversed list (show two different ways).

  lst = [1,2,3,4,5,6,7,8,9,10]
  reversed_list1 = []

  for num in range(len(lst)-1,-1,-1):
    reversed_list1.append(lst[num])
  reversed_list2 = lst[::-1]

  print(f"The sorted list using method-1: {reversed_list1}")
  print(f"The sorted list using method-2: {reversed_list2}")

3. Replace every `"hello"` with `"hi"` in the string `"hello world, hello Python"` and print the result.

  original_string = "hello world, hello Python"
  modified_string = original_string.replace("hello", "hi")
  print(f"The result of the modified original string is: {modified_string}")
  
4. Read a number and print whether it is divisible by both `3` and `5`, by `3` only, by `5` only, or by neither (use proper `if` / `elif` / `else`).
5. Given variables `a = None`, `b = ""`, `c = 0`, `d = "x"`, write code that prints which of these are truthy and which are falsy.
6. Using a ternary expression, assign `"Adult"` if `age >= 18` else `"Minor"`. Print the result.
7. Iterate over the string `"hello"` with `enumerate()` and print index and character on each line.
8. Use `range()` to print all odd numbers from `1` to `19`. Use `for _ in range(...)` (use `_` as the loop variable).
9. Write `is_even(num)` that returns `True`/`False` (single-line return). Include a one-line docstring and one `assert` test.
10. Demonstrate `==` vs `is` with lists: make two lists with the same contents so that `==` is `True` and `is` is `False`. Print both comparisons.
11. Find duplicates in a list **without using `set`** (return duplicates only once, order not important).
12. Use list unpacking to assign `a, b, c, *rest` from `[1,2,3,4,5,6]` and print the variables.
'''

# 3. Replace every `"hello"` with `"hi"` in the string `"hello world, hello Python"` and print the result.



