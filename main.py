'''
⚡ Easy (warm-up)

1 - Take a number input and print its binary form (bin()) and whether it is divisible by 3.
2 - Given the string "Python\nRocks\tHard", print its length and also print it again without escape characters being interpreted (raw string).
3- Create a tuple of numbers, unpack it into variables, and reverse those variables into a new tuple.
'''

num = int(input("Enter a number: "))
for i in range(num,0,-1):
  print('*' * i)