<?php



class Solution
{

    /**
     * @param String $word1
     * @param String $word2
     * @return Boolean
     */
    
    function closeStrings( $word1, $word2 )
    {
        $o = count_chars( $word1, 1 );
        $p = count_chars( $word2, 1 );
        $q = array_keys( $o );
        $r = array_keys( $p );
        $s = array_values( $o );
        $t = array_values( $p );
        sort( $q );
        sort( $r );
        sort( $s );
        sort( $t );
        
        return $q == $r && $s == $t;
    }
    
}



?>
