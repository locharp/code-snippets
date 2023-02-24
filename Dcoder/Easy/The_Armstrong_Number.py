n = int(input())
print('YES' if int((n//100)**3 + (n//10%10)**3 + (n%10)**3) == n else 'NO') 