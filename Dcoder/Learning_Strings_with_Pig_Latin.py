w = input()
print(w + 'way' if w[0] in 'aeiou' else w[1:] + w[0] + 'ay')