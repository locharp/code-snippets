n = input()
a = tuple(map(int, input().split()))
print(a[n//2] if len(a) % 2 else (a[n//2-1] + a[n//2])//2)