class Solution
{



    function search( $nums, $target )
    {
        $i = 0;
        $j = count( $nums ) - 1;

        while ( $i <= $j )
        {
            $k = floor( ( $i + $j ) / 2 );
            
            if ( $nums[$k] < $target )
            {
                $i = $k + 1;
            }
            else
            {
                $j = $k - 1;
            }
        }

        if ( $nums[$i] == $target )
        {
            return $i;
        }
        else
        {
            return -1;
        }
    }
}
