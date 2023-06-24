class Solution
{

    /**
     * @param Integer[] $arr
     * @return Boolean
     */
    function canMakeArithmeticProgression( $arr )
    {
        sort( $arr );
        $n = count( $arr );
        $p = $arr[1] - $arr[0];
        
        for ( $i = 2; $i < $n; $i++ )
        {
            if ( $arr[$i] - $arr[$i - 1] != $p )
            {
                return FALSE;
            }
        }
        
        return TRUE;
    }
}