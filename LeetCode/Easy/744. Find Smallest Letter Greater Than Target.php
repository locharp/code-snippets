class Solution
{

    /**
     * @param String[] $letters
     * @param String $target
     * @return String
     */
    function nextGreatestLetter( $letters, $target )
    {
        $target = ord( $target ) + 1;
        $ordinals = array_map ( "ord", $letters );
        
        while ( $target <= 122 )
        {
            $index = array_search( $target, $ordinals );
            
            if ( is_int ( $index ) )
            {
                break;
            }
            
            $target++;
        }
        
        return $letters[ $index ? $index : 0 ];
    }
}