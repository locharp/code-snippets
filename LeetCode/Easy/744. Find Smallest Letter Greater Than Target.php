class Solution
{
    function nextGreatestLetter( $letters, $target )
    {
        $target = ord( $target ) + 1;
        $ordinals = array_map ( "ord", $letters );
        
        while ( $target <= 122 )
        {
            $index = array_search( $target, $ordinals );
            
            if ( is_int( $index ) )
            {
                break;
            }
            
            $target++;
        }
        
        return $letters[ $index ? $index : 0 ];
    }
}




// 2
class Solution
{
    function nextGreatestLetter( $letters, $target )
    {
        $i = 0;
        $n = count( $letters );
        $j = $n - 1;
        
        while ( $i <= $j )
        {
            $m = floor( ( $i + $j ) / 2 );
            
            if ( $letters[$m] > $target )
            {
                $j = $m - 1;
            }
            else
            {
                $i = $m + 1;
            }
        }
        
        return $letters[ $i % $n ];
    }
}
