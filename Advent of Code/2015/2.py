with open("../datasets/inputs/2.txt") as file:
    inputs = []
    for line in file:
        inputs.append(list(map(int, line.split("x"))))

paper = 0
ribbon = 0
for box in inputs:
    x = box[0] * box[1]
    y = box[1] * box[2]
    z = box[2] * box[0]
    paper += 2 * (x + y + z) + min(x, y, z)
    ribbon += 2 * (sum(box) - max(box)) + (x * box[2])

print("Day 2")
print("Part 1")
print(paper)
print("Part 2")
print(ribbon)