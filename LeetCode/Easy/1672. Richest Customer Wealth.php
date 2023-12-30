<?php



class Solution
{
    /**
     * @param Integer[][] $accounts
     * @return Integer
     */
    
    function maximumWealth( $accounts )
    {
        for ( $i = 0; $i < count( $accounts ); $i++ )
        {
            $accounts[$i] = array_sum( $accounts[$i] );
        }
        
        return max( $accounts );
    }
}



?>
