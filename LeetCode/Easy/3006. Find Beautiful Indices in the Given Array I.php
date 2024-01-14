<?php



class Solution
{
    
    function __construct()
    {
        $this->ans = array();
        $this->i = 0;
        $this->j = -100001;
    }
    
    
    
    /**
     * @param String $s
     * @param String $a
     * @param String $b
     * @param Integer $k
     * @return Integer[]
     */
    
    function beautifulIndices( $s, $a, $b, $k )
    {
        $this->i = strpos( $s, $a, $this->i );
        
        if ( $this->i === FALSE || $this->j === FALSE )
        {
            return $this->ans;
        }
        else if ( $this->i > $this->j + $k )
        {
            $this->j = strpos( $s, $b, max( $this->i - $k, 0 ) );
        }
        else
        {
            if ( $this->i >= $this->j - $k )
            {
                $this->ans[] = $this->i;
            }
            
            if ( $this->i++ > strlen( $s ) - 2 )
            {
                return $this->ans;
            }
        }
        
        return $this->beautifulIndices( $s, $a, $b, $k );
    }
    
}



?>
