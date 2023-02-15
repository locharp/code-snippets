n = int(input())
n += -1 if n < 0 else 1
if n < 0:
  print('1.0,' + ','.join([str(2**i).rstrip('0') for i in range(-1, n, -1)]))
else:
  print(','.join([str(2**i) for i in range(n)]))