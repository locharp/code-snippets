import "sort"

func solution( a []int ) []int
{
	s := make( []int, len( a ) )
    copy( s, a )
    sort.Sort( sort.Reverse( sort.IntSlice( s ) ) )
    
    for i, j := len( a ) - 1, 0; i >= 0; i-- {
        if a[i] == -1 {
            continue
        }
        
        a[i] = s[j]
        j++
    }
    
    return a;
}
