class Solution
{



    function findMin( $nums, $i = 0, $j = null )
    {
        if ( $j === null )
        {
            $j = count( $nums ) - 1;
        }
        
        if ( $nums[$i] <= $nums[$j] )
        {
            return $nums[$i];
        }

        $k = floor( ( $i + $j ) / 2 );
        
        if ( $nums[$i] <= $nums[$k] )
        {
            return $this->findMin( $nums, $k + 1, $j );
        }
        else
        {
            return $this->findMin( $nums, $i, $k );
        }
    }



}
