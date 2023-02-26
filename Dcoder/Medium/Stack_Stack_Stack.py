stack = []
for t in range(int(input())):
  q = input().split()
  if q[0] == 'PUSH':
    stack.append(int(q[1])
  elif q[0] == 'POP':
    stack .pop()
  else:
    print(stack[-1])
print(sum(stack))