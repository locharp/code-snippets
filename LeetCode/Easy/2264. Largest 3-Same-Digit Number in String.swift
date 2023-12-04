class Solution
{
    func largestGoodInteger(_ num: String) -> String
    {
        var s: Set<Character> = []
        var curr: Character = " "
        var count = 0
        
        for char in num
        {
            if char == curr {
                count = count + 1

                if count > 2
                {
                    s.insert( char )
                }
            }
            else
            {
                curr = char
                count = 1
            }
        }

        if let ans = s.max()
        {
            return String( repeating: ans, count: 3 )
        }
        else
        {
            return ""
        }
    }
}
