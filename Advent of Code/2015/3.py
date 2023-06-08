print("Day 3")
print("Part 1")
inp = ""
with open("../datasets/inputs/3.txt") as file:
    inp = file.readline()

x = 0
y = 0
houses = {(0, 0): 1}
for move in inp:
    if move == "^":
        y += 1
    elif move == "v":
        y -= 1
    elif move == ">":
        x += 1
    elif move == "<":
        x -= 1

    if (x, y) not in houses:
        houses[(x, y)] = 0

    houses[(x, y)] += 1

print(len(houses))

# Part 2
print("Part 2")

x = [0, 0]
y = [0, 0]
santa = 0
houses = {(0, 0): 2}
for move in inp:
    if move == "^":
          y[santa] += 1
    elif move == "v":
        y[santa] -= 1
    elif move == ">":
        x[santa] += 1
    elif move == "<":
        x[santa] -= 1

    if (x[santa], y[santa]) not in houses:
        houses[(x[santa], y[santa])] = 0

    houses[(x[santa], y[santa])] += 1

    santa = (santa + 1) %2

print(len(houses))