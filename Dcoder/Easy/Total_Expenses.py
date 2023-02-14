for t in range(int(input())):
  e = float(input())
  print("{0:.2f}".format(e * .9 if e > 1000 else e))