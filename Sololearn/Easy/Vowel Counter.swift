let vowels = "AEIOUaeiou"
let input = readLine()!
var ans = 0

input.forEach { ch in
    if vowels.contains( ch )
    {
        ans = ans + 1
    }
}

print( ans )
