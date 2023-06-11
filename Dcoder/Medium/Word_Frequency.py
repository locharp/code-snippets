input()
words = input().split()
ordered = {}
for word in words:
    if word not in ordered:
        ordered[word] = words.count( word )

print( " ".join( sorted( ordered, key=lambda k: ordered[k], reverse=True) ) )