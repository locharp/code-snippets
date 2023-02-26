s = input()
compressed, tmp, repeated = '',  '', 0
for ch in s:
  if ch == tmp:
    repeated += 1
  else:
    compressed += tmp + (str(repeated) if repeated > 1 else '')
    tmp = ch
    repeated = 1
compressed += ch + (str(repeated) if repeated > 1 else '')
print(compressed if len(compressed) < len(s) else s)