x1, y1, x2, y2 = map(int, input().split())
print('A' if (x1**2 + y1**2)**.5 < (x2**2 + y2**2)**.5 else 'B')