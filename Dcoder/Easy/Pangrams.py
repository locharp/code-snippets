from string import ascii_uppercase
s = input().upper()
print('YES' if all(ch in s for ch in ascii_uppercase) else 'NO') 