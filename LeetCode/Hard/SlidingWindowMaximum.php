class Solution
{
    function maxSlidingWindow( $nums, $k )
    {
        $maxes = array();
        $window = array();
      
        for ( $i = 0; $i < count( $nums ); $i++  )         {
            if ( $nums[$i] >= $nums[$window[0]] )
            {
                $window = array ( $i );
            }
            else
            {
                if ( $i - $k >= $window[0] )
                {
                    array_shift( $window );
                }

                while ( !empty( $window) && $nums[end( $window )] <= $nums[$i] )
                {
                    array_pop( $window );
                }
            
                array_push( $window, $i );
            }
        
            if ( $i >= $k - 1 )
            {
                array_push( $maxes, $nums[$window[0]] );
            }
        }

        return $maxes;
    }
}