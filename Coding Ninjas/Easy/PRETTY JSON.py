def prettyJSON( str ):

    ind = 0
    s = ""
    ans = []

    for ch in str:
        if ch == "{" or ch == "[":
            if s != "":
                ans.append( " " * ind + s )
                s = ""
                
            ans.append( " " * ind + ch )
            ind += 4
        elif ch == "}" or ch == "]":
            ans.append( " " * ind + s )
            s = ""
            ind -= 4
            ans.append( " " * ind + ch )
        elif ch == ",":
            if ans[-1][-1] == "}" or ans[-1][-1] == "]":
                ans[-1] += ch
            else:
                ans.append( " " * ind + s + ch )
                s = ""
        else:
            s += ch
            
    return ans
