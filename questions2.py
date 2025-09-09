'''
# EASY — check the basics (1–2 lines each)

1. Write a program that reads an integer from `input()` and prints `"Even"` or `"Odd"`. Handle `0` and negative numbers correctly.
2. Create a list of numbers from `1` to `10`, reverse it, and print the reversed list (show two different ways).
3. Replace every `"hello"` with `"hi"` in the string `"hello world, hello Python"` and print the result.
4. Read a number and print whether it is divisible by both `3` and `5`, by `3` only, by `5` only, or by neither (use proper `if` / `elif` / `else`).
5. Given variables `a = None`, `b = ""`, `c = 0`, `d = "x"`, write code that prints which of these are truthy and which are falsy.
6. Using a ternary expression, assign `"Adult"` if `age >= 18` else `"Minor"`. Print the result.
7. Iterate over the string `"hello"` with `enumerate()` and print index and character on each line.
8. Use `range()` to print all odd numbers from `1` to `19`. Use `for _ in range(...)` (use `_` as the loop variable).
9. Write `is_even(num)` that returns `True`/`False` (single-line return). Include a one-line docstring and one `assert` test.
10. Demonstrate `==` vs `is` with lists: make two lists with the same contents so that `==` is `True` and `is` is `False`. Print both comparisons.
11. Find duplicates in a list **without using `set`** (return duplicates only once, order not important).
12. Use list unpacking to assign `a, b, c, *rest` from `[1,2,3,4,5,6]` and print the variables.

---

# MEDIUM — combine topics and “real” cases

1. `count_vowels(s)` — write a function that returns a dictionary with counts for each vowel (`a,e,i,o,u`) **case-insensitive**. Keys should be lowercase.
2. Given `d = {'a':[1,2], 'b':[3]}`, safely print the 2nd element of key `'a'` and handle a missing key `'z'` without raising an error (use dict methods).
3. Use the **walrus operator** to read integers repeatedly until the user enters `0`, and print the running sum when loop ends. (One-line `while` condition should use `:=`.)
4. Implement `transpose(matrix)` for a rectangular 2D list using nested `for` loops (do NOT use `zip`). Example: `[[1,2,3],[4,5,6]] -> [[1,4],[2,5],[3,6]]`.
5. Write `compute_stats(*nums, round_digits=2, **kwargs)` that returns a tuple `(min, max, avg)` for numeric `nums`. Include a docstring explaining params and return. (Handle zero arguments gracefully.)
6. Implement `rotate_right(lst, k)` that rotates list `lst` to the right by `k` positions **in-place** (mutate original list). Use slicing/augmented assignment.
7. Given a string and a substring, return a list of start indices where substring occurs (overlapping occurrences allowed). Use a loop (no regex).
8. Merge two dicts of lists: `d1` and `d2` where values are lists — if a key exists in both, extend the list; else add the key. Return the merged dict.
9. Return the **first non-repeating** element from a list (value, not index). If none, return `None`. (Use a dictionary for counts.)
10. Write a small `while` loop that reads commands from `input()` until `"exit"`; for each integer command, skip negatives with `continue`, stop processing if value > 100 using `break`, and use `pass` as a placeholder when command is an empty line. Print actions performed.
11. Given `name` and `age`, print `"Name: <name>\tAge: <age>\n"` using an f-string and escape sequences.
12. Show the difference between copying a list by reference and copying by slicing: modify the child list in both cases and print the parent list to demonstrate behavior.

---

# HARD — multi-topic interview-style challenges

1. **Closures & nonlocal** — Implement `make_counter()` that returns `increment()`; each call to `increment()` increases an internal counter and returns it. Show two independent counters to prove closure isolation. (Use `nonlocal`.)
2. **Scope & fix the bug** — You’re given:

   ```py
   def outer():
       x = 0
       def inner():
           x += 1
           return x
       return inner()
   ```

   Explain why it fails and **fix it** using the minimal change required to make `outer()` return `1`. (Provide code that works.)
3. **Group by** — Given a list of dicts like ` [{'name':'A','age':30}, {'name':'B','age':30}, {'name':'C','age':25}]`, write a function that returns a dict grouping names by age: `{30:['A','B'], 25:['C']}`. Preserve insertion order of names.
4. **Duplicate summary** — Implement `duplicate_counts(lst)` that returns a list of tuples `(value, count)` **for values that appear more than once**, sorted by count descending. Do **not** use `collections.Counter`.
5. **Immutable result** — Write `flatten_to_tuple(matrix)` that flattens a 2D list into a single **tuple** (immutable) preserving row-major order. Show that returned value is immutable by attempting an invalid operation in comments.
6. **Common elements preserving order** — Given `a` and `b` (both lists), return a new list of elements that are present in both, preserving the order from `a`, and without using sets or `&` operators. (Example: `[1,2,3,2]` & `[2,3]` -> `[2,3,2]` or clarify how you handle counts.) Implement with preserved multiplicity.
7. **Robust conversion** — Given a list of strings `["1", "2.5", "x", "4"]`, write `safe_mean(strs)` that converts valid numeric strings to floats, ignores invalids, and returns average as a `float`. If no valid numbers, return `None`. Use `try/except` to avoid crashing.
8. **Command loop simulator** — Build a simple command processor that supports:

   * `"PUSH n"` — push integer `n` onto a stack
   * `"POP"` — pop from stack (ignore if empty)
   * `"TOP"` — print top element or `"EMPTY"`
   * `"EXIT"` — stop processing
     Read commands until `"EXIT"` using a `while` loop; handle invalid commands gracefully (print `"INVALID"`). Use `split()` to parse.
9. **Walrus in practice** — Read lines until a blank line is entered; use walrus to append non-empty, stripped lines to a list in the `while` condition. After loop, print the list.
10. **Shallow copy vs reference** — Create a nested list `parent = [[1],[2]]`. Create `child_ref = parent` and `child_copy = parent[:]`. Mutate `child_ref[0].append(99)` and `child_copy[1] = [7]`. Print `parent` after both ops and explain (in a one-line comment) which mutation affected `parent` and why.
11. **Pairs from list** — Write `all_pairs(lst)` that returns a list of all unique unordered pairs `(a,b)` where `a != b` from `lst` (each pair should appear once, e.g., `(1,2)` but not `(2,1)` if both exist). Use loops only.
12. **Small unit tests** — For your `is_even` and `rotate_right` functions (from earlier), write 3 `assert` statements each that test normal and edge cases (e.g., empty list, k = 0, negative k if you choose to support it). Place these `assert`s under `if __name__ == "__main__":`.
13. **Clean-code refactor** — Take any medium-level solution you wrote above and refactor it into a small, well-documented function with clear variable names, a docstring, and no repeated code (DRY). Paste the original purpose as a one-line comment and then the refactored function.
14. **Edge-case thinker** — Write a single function `unique_or_first(lst)` that returns the only element if `lst` contains exactly one unique value (e.g., `[2,2,2] -> 2`), otherwise returns the first element that is unique (occurs once). If none unique, return `None`. Keep solution O(n).

'''

################################################################################################################################################################

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

  print(f"The reversed list using method-1: {reversed_list1}")
  print(f"The reversed list using method-2: {reversed_list2}")

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
  if b:
    print(f"If this is printed, then b value {b} is TRUTHY")
  if c:
    print(f"If this is printed, then c value {c} is TRUTHY")
  if d:
    print(f"If this is printed, then d value {d} is TRUTHY")

6. Using a ternary expression, assign `"Adult"` if `age >= 18` else `"Minor"`. Print the result.

  age = int(input("Enter the age: "))
  result = "Adult" if age >= 18 else "Minor"

  print(f"The entered age {age} falls under {result} category.")

7. Iterate over the string `"hello"` with `enumerate()` and print index and character on each line.

  string = "hello"
  for index,char in enumerate(string):
    print(f"The value of {char} is stored in the index position {index}")

8. Use `range()` to print all odd numbers from `1` to `19`. Use `for _ in range(...)` (use `_` as the loop variable).

  for _ in range(1,20,2):
    print(f"The number {_} is an odd number")

9. Write `is_even(num)` that returns `True`/`False` (single-line return). Include a one-line docstring and one `assert` test.

  def is_even(num):
    """Return True if num is even, False otherwise."""
    return num % 2 == 0

  # Assertions (they should pass silently if correct)
  assert is_even(10) == True
  assert is_even(3) == False
  assert is_even(0) == True

  print("All tests passed!")


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

  a,b,c, *rest = [1,2,3,4,5,6]
  print(f"The value of a is: {a}")
  print(f"The value of b is: {b}")
  print(f"The value of c is: {c}")
  print(f"The value of rest is: {rest}")

'''