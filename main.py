# 2. Given a list of integers, return a dictionary with the number as the key and its frequency as the value.

lst = [1,2,3,4,5,6,5,1,2,3,4,7,8,8,7,9]

result = {}

for num in lst:
  if num in result:
    result[num] += 1
  else:
    result[num] = 1

print(f"The count of given list of numbers: {result}")