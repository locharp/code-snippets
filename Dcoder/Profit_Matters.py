arr = sorted(map(int, input()[1:-1].split(',')))
print(arr if len(arr) == 1 else f'[{min(arr)},{max(arr)}]')