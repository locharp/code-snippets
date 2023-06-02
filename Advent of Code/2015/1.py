print('Part 1')
inp = ''
with open('../datasets/input/1.txt') as file:
    inp = file.readline()
    
print(inp.count('(') - inp.count(')'))

print('Part 2')
floor = 0
for i in range(len(inp)):
    if inp[i] == '(':
        floor += 1
    else:
        floor -= 1
    
    if floor < 0:
        print(i + 1)
        break