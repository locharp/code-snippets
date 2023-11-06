from math import *

def stringPair( n: int, nums: [int] ) -> chr:
    c = { 0: "zero", 1: "one", 2: "two", 3: "three", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 
        30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 
        80: "eighty", 90: "ninty", 100: "hundred", 101: "greater 100" }
    
    d = { 1: 2, 2: 1, 3: 2, 4: 2, 5: 2, 
        6: 1, 7: 2, 8: 2, 9: 2, 10: 1, 
        11: 3, 12: 2, 13: 3, 14: 4, 15: 3, 
        16: 3, 17: 4, 18: 4, 19: 4, 20: 1,
        30: 1, 40: 1, 50: 1, 60: 1, 70: 2, 
        80: 2, 90: 1, 100: 2 }

    u = v = 0
    
    for num in nums:
        if num < 21:
            v += d[num]
        else:
            v += d[ floor( num / 10 ) * 10 ] + d[ num % 10 ]

    for i in range( n ):
        for j in nums[ i + 1 : ]:
            if nums[i] + j == v:
                u += 1

    if u < 21:
        return c[u]
    elif u > 100:
        return c[101]
    else:
        return c[ floor( u / 100 ) * 10 ] + "-" + c[ u % 10 ]
