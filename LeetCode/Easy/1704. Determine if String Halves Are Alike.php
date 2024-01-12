<?php



class Solution
{

    function halvesAreAlike( $s )
    {
        $vowels = "AEIOUaeiou";
        $n = strlen( $s );
        $m = $n / 2;
        $p = $q = 0;

        for ( $i = 0; $i < $m; $i++ )
        {
            if ( str_contains( $vowels, $s[$i] ) )
            {
                $p++;
            }
        }

        for ( $i = $m; $i < $n; $i++ )
        {
            if ( str_contains( $vowels, $s[$i] ) )
            {
                $q++;
            }
        }

        return $p == $q;
    }
  
}



?>
