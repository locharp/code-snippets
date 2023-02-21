v = 0
for i in range(int(input())):
  s = input()
  if s[0] in '^_' and s[-1] in '_^':
    v += 1
print(v)