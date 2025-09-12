'''
10. Write a function `transpose(matrix)` that returns the transpose of a 2D list (matrix). Do **not** use built-in libraries like NumPy. Example: `[[1,2,3],[4,5,6]] → [[1,4],[2,5],[3,6]]`

    nested_list = [[1,2,3],[4,5,6]]
    result = []

    for value in range(0, len(nested_list[0])):
      temp = []
      for row in nested_list:
          temp.append(row[value])
      result.append(temp)

    print(f"The final pair of the given nested list is: {result}")

11. Write a function `find_vowel_count(s)` that returns a dictionary of vowel counts from a string (case-insensitive). Example: `"Anand"` → `{'a':2}`.

    vowels = 'aeiou'
    def find_vowels_count(s):
        vowel_count = {}
        for char in s.lower():
            if char in vowels:
                result[char] = s.lower().count(char)
        return vowel_count

    result = find_vowels_count('Anand')
    print(f"The vowel count of given string: {result}")

12. Write a program that:

* Takes a list of numbers from the user.
* Prints the sum of only the even numbers.
* If the list is empty, print `"No numbers provided"`.

13. Write a function `find_common_elements(list1, list2)` that returns a sorted list of elements that appear in both lists, **without duplicates**. Example: `[1,2,3,3]` and `[2,3,4]` → `[2,3]`.
14. Write a function `is_palindrome(s)` that checks if a string is a palindrome (ignores case and spaces). Example: `"Race car"` → `True`.
15. (Scope + Functions) Write a nested function `outer()` that defines a variable `x = 10`. Inside it, define an `inner()` function that modifies `x` using `nonlocal`. Call both and print the modified `x`.
'''

# 11. Write a function `find_vowel_count(s)` that returns a dictionary of vowel counts from a string (case-insensitive). Example: `"Anand"` → `{'a':2}`.




