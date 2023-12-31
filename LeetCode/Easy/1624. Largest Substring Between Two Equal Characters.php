<?php



class Solution
{

    /**
     * @param String $s
     * @return Integer
     */

    function maxLengthBetweenEqualCharacters( $s )
    {
        $ans = -1;
        $a = array();

        foreach ( str_split( $s ) as $i => $j )
        {
            if ( key_exists( $j, $a ) )
            {
                $ans = max( $ans, $i - $a[$j] );
            }
            else
            {
                $a[$j] = $i + 1;
            }
        }

        return $ans;
    }
}



?>
