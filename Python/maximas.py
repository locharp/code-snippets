number_of_points = 0
while number_of_points < 2:
    number_of_points = int(input('Please enter the number of points (2 or more): '))

# Create a dict to save the points
# x as the keys, y as the values
points = {}
for i in range(number_of_points):
    x, y = map(int, input().split())
    if x not in points:
        points[x] = []
    points[x] += [ y ]

# sort the dict by x and keep only the highest y
points = { key: max(value) for key, value in sorted(points.items(), key=lambda element: element, reverse=True) }

# Create a list to save the maximal points
# Pop the one with the highest x as the first point
maximal_points = [ (max(points), points[max(points)]) ]

# Loop through the rest and append the points with y higher than the current max
for key, value in points.items():
    if value > maximal_points[-1][1]:
        maximal_points.append((key, value))

print('count: ', len(maximal_points))
print(maximal_points)