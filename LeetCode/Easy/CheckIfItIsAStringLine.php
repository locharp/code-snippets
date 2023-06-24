class Solution
{

    /**
     * @param Integer[][] $coordinates
     * @return Boolean
     */
    function r( $p, $q )
    {
        $x = $q[0] - $p[0];
        $y = $q[1] - $p[1];
        
        if ( $x == 0 )
        {
            if ( $y == 0 )
            {
                return 0;
            }
            else
            {
                return "INFINITY";
            }
        }
        
        return ( $q[1] - $p[1] ) / ( $q[0] - $p[0] );
    }
    
    function checkStraightLine( $coordinates )
    {
        $m = $this->r( $coordinates[0], $coordinates[1] );
        $n = count( $coordinates );
        
        for ( $i = 2; $i < $n; $i++ )
        {
            if ( $this->r( $coordinates[$i], $coordinates[$i - 1] ) != $m )
            {
                return FALSE;
            }
        }
        
        return TRUE;
    }
}