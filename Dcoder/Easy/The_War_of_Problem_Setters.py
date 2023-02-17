d = sum(map(int, input().split())) - sum(map(int, input().split()))
if d == 0:
  print('None 0')
elif d > 0:
  print('Garry', d)
else:
  print('Sharry', -d)