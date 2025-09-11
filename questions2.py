'''
## 🟢 Easy (warm-up, direct checks)

1. Write a Python program that checks if a given number is divisible by both 3 and 5. Print `"FizzBuzz"` if true, else print the number itself.
2. Given a list of numbers `[2, 4, 6, 8, 10]`, write a function `is_even_list(lst)` that returns `True` if **all** numbers are even, otherwise `False`.
3. Take a string input from the user and check whether it is empty (hint: truthy/falsy). If empty, print `"Empty string"`, else print `"Non-empty string"`.
4. Write a function `greet(name, emoji=":)")` that prints a greeting. Demonstrate calling it with positional arguments, keyword arguments, and default arguments.

---

## 🟡 Medium (mixing multiple concepts)

5. Write a program that counts how many times each word appears in the string:
   `"Python is great and Python is fun"`. Store the result in a dictionary.
6. Given a list `nums = [1, 2, 3, 4, 5]`, use a **for loop with enumerate** to print the index and the square of each number.
7. Write a program to find duplicates in a list without using a set. Example: `[1,2,3,2,4,5,1] → [1,2]`.
8. Create a dictionary `user = {"name": "Anand", "age": 33, "skills": ["Python", "SQL"]}`.

   * Loop through the dictionary and print keys and values.
   * Add a new key `"location"` with any value.
   * Remove `"age"`.
9. Write a function `calculate_total(*args, **kwargs)` that:

   * Adds up all positional arguments (numbers).
   * Then adds values from keyword arguments.
     Example: `calculate_total(1,2,3, x=4, y=5)` → `15`.

---

## 🔴 Hard (interview-style, combined)

10. Write a function `transpose(matrix)` that returns the transpose of a 2D list (matrix). Do **not** use built-in libraries like NumPy. Example:
    `[[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]`.
11. Write a function `find_vowel_count(s)` that returns a dictionary of vowel counts from a string (case-insensitive). Example: `"Anand"` → `{'a':2}`.
12. Write a program that:

* Takes a list of numbers from the user.
* Prints the sum of only the even numbers.
* If the list is empty, print `"No numbers provided"`.

13. Write a function `find_common_elements(list1, list2)` that returns a sorted list of elements that appear in both lists, **without duplicates**. Example: `[1,2,3,3]` and `[2,3,4]` → `[2,3]`.
14. Write a function `is_palindrome(s)` that checks if a string is a palindrome (ignores case and spaces). Example: `"Race car"` → `True`.
15. (Scope + Functions) Write a nested function `outer()` that defines a variable `x = 10`. Inside it, define an `inner()` function that modifies `x` using `nonlocal`. Call both and print the modified `x`.

'''