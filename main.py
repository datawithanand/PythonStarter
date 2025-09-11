'''
5. Write a program that counts how many times each word appears in the string: `"Python is great and Python is fun"`. Store the result in a dictionary.

  string = "Python is great and Python is fun"
  result = {}
  for word in string.split(" "):
    result[word] = string.count(word)

  print(f"The number of times each word repeated is: {result}")
  
6. Given a list `nums = [1, 2, 3, 4, 5]`, use a **for loop with enumerate** to print the index and the square of each number.

  nums = [1, 2, 3, 4, 5]
  for index,num in enumerate(nums):
    print(f"The index value of {num} is {index} and the square is: {num*num}")

7. Write a program to find duplicates in a list without using a set. Example: `[1,2,3,2,4,5,1] → [1,2]`.
8. Create a dictionary `user = {"name": "Anand", "age": 33, "skills": ["Python", "SQL"]}`.

   * Loop through the dictionary and print keys and values.
   * Add a new key `"location"` with any value.
   * Remove `"age"`.
9. Write a function `calculate_total(*args, **kwargs)` that:

   * Adds up all positional arguments (numbers).
   * Then adds values from keyword arguments.
     Example: `calculate_total(1,2,3, x=4, y=5)` → `15`.
'''
# Given a list `nums = [1, 2, 3, 4, 5]`, use a **for loop with enumerate** to print the index and the square of each number.

