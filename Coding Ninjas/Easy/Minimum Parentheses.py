def minimumParentheses( pattern ):

    ans = o = 0
    
    for i in pattern:
        if i == "(":
            o += 1
        elif o > 0:
            o -= 1
        else:
            ans += 1

    return ans + o
