func strToDict( s: String ) -> [ Character : Int ]
{
    var dict: [ Character : Int ] = [ Character : Int ]()
    
    for ch in s
    {
        if dict.keys.contains( ch )
        {
            dict[ch]! += 1
        }
        else
        {
            dict[ch] = 1
        }
    }
    
    return dict
}



func solution( s1: String, s2: String ) -> Int
{
    var count = 0
    let dict1 = strToDict( s: s1 )
    let dict2 = strToDict( s: s2 )
    
    for ( ch, val ) in dict1 {
        count += min( val, dict2[ch] ?? 0 )
    }
    
    return count
}
