a, b, c = map(float, input().split())
discriminant = (b**2 - 4*a*c)
print(' ' if discriminant < 0 else '{0:.2f}'.format(-b/a))