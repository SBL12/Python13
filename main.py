 # Write a program that uses a loop fill an empty list with 10 numbers and prints the list to the console. The numbers can be random or simply put in the numbers 0-9 or 1-10 in ascending order.

import random
list2 = []
for i in range (10):
  list2.append(random.randint(0,99))
print(list2)
list2.sort()
print(list2)