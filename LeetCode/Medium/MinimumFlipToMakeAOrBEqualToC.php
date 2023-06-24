class Solution
{

    /**
     * @param Integer $a
     * @param Integer $b
     * @param Integer $c
     * @return Integer
     */
    function minFlips( $a, $b, $c )
    {
        $a = decbin( $a );
        $b = decbin( $b );
        $c = decbin( $c );
        $len = max( strlen( $a ), strlen( $b ), strlen( $c ) );
        $a = str_pad( $a, $len, "0", STR_PAD_LEFT );
        $b = str_pad( $b, $len, "0", STR_PAD_LEFT );
        $c = str_pad( $c, $len, "0", STR_PAD_LEFT );
        $flips = 0;
        
        for ( $i = 0; $i < $len; $i++ )
        {
            if ( $c[$i] == "0" )
            {
                $flips += (int) $a[$i] + (int) $b[$i];
            }
            else
            {
                if ( $a[$i] == "0" && $b[$i] == "0" )
                {
                    $flips++;
                }
            }
        }
        
        return $flips;
    }
}