lst = []
for t in range(int(input())):
  lst.append(input())
for password in lst:
  if password[::-1] in lst:
    print(len(password), password[len(password)//2])
    break