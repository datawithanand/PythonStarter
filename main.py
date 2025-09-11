# MEDIUM — combine topics and “real” cases
'''
1. `count_vowels(s)` — write a function that returns a dictionary with counts for each vowel (`a,e,i,o,u`) **case-insensitive**. Keys should be lowercase.

  vowels ='aeiouAEIOU'
  result = {}

  def vowel_count(string):
    for char in string:
      if char.isalpha() and char in vowels:
        result[char.lower()] = string.count(char)

  vowel_count('hEllo')
  print(f"The number of vowels in the given string is: {result}")

2. Given `d = {'a':[1,2], 'b':[3]}`, safely print the 2nd element of key `'a'` and handle a missing key `'z'` without raising an error (use dict methods).

  d = {'a':[1,2], 'b':[3]}
  print(f"The value of second element of key[a] is : {d['a'][1]}")
  z_value = d.get('z','Not found')
  print(f"The value of z-elementis : {z_value}")

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
'''
# 3. Use the **walrus operator** to read integers repeatedly until the user enters `0`, and print the running sum when loop ends. (One-line `while` condition should use `:=`.)



