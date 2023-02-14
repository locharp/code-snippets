m = int(input())
d = {i[1]:i[0] for i in (tuple(map(int, input().split())), tuple(map(int, input().split())))}
if m >= sum(d):
  print(sum(d.values()))
elif m >= max(d):
  print(d[max(d)])
elif m >= min(d):
  print(d[min(d)])
else:
  print(0)