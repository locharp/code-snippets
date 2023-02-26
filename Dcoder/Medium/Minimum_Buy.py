from functools import reduce
for t in range(int(input())):
  fruits = {}
  for fruit in input():
    if fruit not in fruits:
      fruits[fruit] = 0
    fruits[fruit] += 1
  print(reduce(lambda cost, value: cost + (value + 1) // 2, fruits.values(), 0))