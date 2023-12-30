<?php



class Solution
{
    function makeEqual( $words )
    {
        $n = count( $words );
        $a = array();

        foreach ( $words as $word )
        {
            foreach ( str_split( $word ) as $ch )
            {
                if ( key_exists( $ch, $a ) )
                {
                    $a[$ch] += 1;
                }
                else
                {
                    $a[$ch] = 1;
                }
            }
        }

        foreach( $a as $c )
        {
            if ( $c % $n != 0 )
            {
                return FALSE;
            }
        }

        return TRUE;
    }
}



?>
