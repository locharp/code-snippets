century = (int(input()) + 99) // 100
suffix = 'th'
if century // 10 != 1: 
  if century % 10 == 1:
    suffix = 'st'
  elif century % 10 == 2:
    suffix = 'nd'
  elif century % 10 == 3:
    suffix = 'rd'
print(str(century) + suffix)