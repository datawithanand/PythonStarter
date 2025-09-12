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

##########################################################################################################################################################################################

'''
1. Write a Python program that checks if a given number is divisible by both 3 and 5. Print `"FizzBuzz"` if true, else print the number itself.

  number = int(input("Enter a number to check if it's divisble by 3 and 5: "))
  if number%3 == 0 and number%5 == 0:
    print("FizzBuzz")
  else:
    print(number)

2. Given a list of numbers `[2, 4, 6, 8, 10]`, write a function `is_even_list(lst)` that returns `True` if **all** numbers are even, otherwise `False`.

  def is_even_list(lst):
    return all(num %2 ==0 for num in lst)

  result = is_even_list([2, 4, 6, 8, 10])
  print(result)

3. Take a string input from the user and check whether it is empty (hint: truthy/falsy). If empty, print `"Empty string"`, else print `"Non-empty string"`.

  string = input("Enter a string: ")
  if string:
    print("Non-empty string")
  else:
    print("Empty string")

4. Write a function `greet(name, emoji=":)")` that prints a greeting. Demonstrate calling it with positional arguments, keyword arguments, and default arguments.

  def greet(name, emoji=":)"):
    return f"Hello, {name}. We are glad to have you here {emoji}"

  positional_example = greet('Anand', ':(')
  keyword_example = greet(emoji=':(', name='Anand')
  default_example = greet('Anand')

  print(f"The positional argument result: {positional_example}")
  print(f"The keyword argument result: {keyword_example}")
  print(f"The default argument result: {default_example}")

'''
##########################################################################################################################################################################################

'''
5. Write a program that counts how many times each word appears in the string: `"Python is great and Python is fun"`. Store the result in a dictionary.

  string = "Python is great and Python is fun"
  result = {}

  for word in string.split():   # split already handles spaces
      if word in result:
          result[word] += 1
      else:
          result[word] = 1

  print(result)

6. Given a list `nums = [1, 2, 3, 4, 5]`, use a **for loop with enumerate** to print the index and the square of each number.

  nums = [1, 2, 3, 4, 5]
  for index,num in enumerate(nums):
    print(f"The index value of {num} is {index} and the square is: {num*num}")

7. Write a program to find duplicates in a list without using a set. Example: `[1,2,3,2,4,5,1] → [1,2]`

  lst = [1,2,3,2,4,5,1]
  dup_list = []
  for num in lst:
    if lst.count(num) > 1:
      if num not in dup_list:
        dup_list.append(num)

  print(f"The duplicate list is: {dup_list}")

8. Create a dictionary `user = {"name": "Anand", "age": 33, "skills": ["Python", "SQL"]}`.
   Loop through the dictionary and print keys and values. Add a new key `"location"` with any value. Remove `"age"`.

  user = {"name": "Anand", "age": 33, "skills": ["Python", "SQL"]}
  user['location'] = 'Chennai'
  del user['age']
  for key,value in user.items():
    print(f"The key is: {key} and the value is: {value}")

9. Write a function `calculate_total(*args, **kwargs)` that:
   Adds up all positional arguments (numbers). Then adds values from keyword arguments. Example: `calculate_total(1,2,3, x=4, y=5)` → `15`.

    def calculate_total(*args, **kwargs):
      count = 0
      for index in range(0,len(args)):
        count += args[index]
      for key,value in kwargs.items():
        count += value
      return count

    result = calculate_total(1,2,3, x=4, y=5)
    print(f"The sum of the numbers: {result}")
'''

##########################################################################################################################################################################################

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
                vowel_count[char] = vowel_count.get(char, 0) + 1
        return vowel_count

    result = find_vowels_count('Anand')
    print(f"The vowel count of given string: {result}")


12. Write a program that: Takes a list of numbers from the user. Prints the sum of only the even numbers. If the list is empty, print `"No numbers provided"`.

    def sum_even_nums(lst):
        sum_even_count = 0
        if not lst:
            return 'No numbers provided'
        for num in lst:
            if num %2 ==0 :
                sum_even_count += num
        return sum_even_count

    result = sum_even_nums([])
    print(f"The sum of even numbers list is: {result}")

13. Write a function `find_common_elements(list1, list2)` that returns a sorted list of elements that appear in both lists, **without duplicates**. Example: `[1,2,3,3]` and `[2,3,4]` → `[2,3]`.

    def find_common_elements(list1, list2):
        result = []
        for num in list1:
            if num in list2:
                if num not in result:
                    result.append(num)
        return sorted(result)

    print(find_common_elements([1,2,3,3], [2,3,4]))

14. Write a function `is_palindrome(s)` that checks if a string is a palindrome (ignores case and spaces). Example: `"Race car"` → `True`.

    def is_palindrome(s):
        return s.lower().replace(" ","") == s.lower().replace(" ","")[::-1]

    string = "Race car"
    result = is_palindrome(string)
    print(result)

15. (Scope + Functions) Write a nested function `outer()` that defines a variable `x = 10`. Inside it, define an `inner()` function that modifies `x` using `nonlocal`. Call both and print the modified `x`.

    def outer_fun():
        x = 10
        print(f"x value before modified: {x}")
        def inner_fun():
            nonlocal x
            x = 20
            print(f"x value inside inner_fun: {x}")
        inner_fun()

    outer_fun()

'''