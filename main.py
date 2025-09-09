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

  num = int(input("Enter a number to check if it's divisble by 3 & 5: "))

  if num % 3 == 0 and num % 5 == 0:
    print("The entered number is divisble by both 3 and 5.")
  elif num % 3 == 0 and not num % 5 == 0:
    print("The entered number is divisble by 3 but not by 5.")
  elif not (num % 3 == 0) and num % 5 == 0:
    print("The entered number is divisble by 5 but not by 3.")
  else:
    print("The entered number is neither divisble by 3 or 5.")

5. Given variables `a = None`, `b = ""`, `c = 0`, `d = "x"`, write code that prints which of these are truthy and which are falsy.

  a,b,c,d = None, "", 0, "x"

  if a:
    print(f"If this is printed, then a value {a} is TRUTHY")
  elif b:
    print(f"If this is printed, then b value {b} is TRUTHY")
  elif c:
    print(f"If this is printed, then c value {c} is TRUTHY")
  else:
    print(f"If this is printed, then d value {d} is TRUTHY")

6. Using a ternary expression, assign `"Adult"` if `age >= 18` else `"Minor"`. Print the result.

  age = int(input("Enter the age: "))
  result = "Adult" if age >= 18 else "minor"

  print(f"The entered age {age} falls under {result} category.")

7. Iterate over the string `"hello"` with `enumerate()` and print index and character on each line.

  string = "hello"
  for index,num in enumerate(string):
    print(f"The value of {num} is stored in the index position {index}")

8. Use `range()` to print all odd numbers from `1` to `19`. Use `for _ in range(...)` (use `_` as the loop variable).

  for _ in range(1,20):
    if _ %2 == 0:
      pass
    else:
      print(f"The number {_} is an odd number")

9. Write `is_even(num)` that returns `True`/`False` (single-line return). Include a one-line docstring and one `assert` test.

  def is_even(num): # Asset test is not written since it was not covered in my reading list
    
    Args: num is an integer number 
  
    return num % 2 == 0
  
  print(is_even(10))

10. Demonstrate `==` vs `is` with lists: make two lists with the same contents so that `==` is `True` and `is` is `False`. Print both comparisons.

  lst1 = [1,2,3]
  lst2 = [1,2,3]

  print(f"The lst1 and lst2 has same values or not: {lst1 == lst2}")
  print(f"The lst1 and lst2 has same memory location or not: {lst1 is lst2}")

11. Find duplicates in a list **without using `set`** (return duplicates only once, order not important).

  lst = [1,2,3,1,2,4,5,3,7,6,3,2,1,2,3,4]
  dup_lst = []

  for num in lst:
    if lst.count(num) > 1:
      if num not in dup_lst:
        dup_lst.append(num)

  print(f"The duplicate values in the given list: {dup_lst}")

12. Use list unpacking to assign `a, b, c, *rest` from `[1,2,3,4,5,6]` and print the variables.
'''

# 12. Use list unpacking to assign `a, b, c, *rest` from `[1,2,3,4,5,6]` and print the variables.

a,b,c, *rest = [1,2,3,4,5,6]
print(f"The value of a is: {a}")
print(f"The value of b is: {b}")
print(f"The value of c is: {c}")
print(f"The value of rest is: {rest}")




