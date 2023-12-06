class Solution
{
    function totalMoney( $n )
    {
        $m = floor( $n / 7 );
        $o = $n % 7;
        
        return ( floor( $m * ( $m + 1 ) / 2 ) * 7 ) + ( 21 * $m ) + floor( $o * ( $o + 1 ) / 2 ) + ( $o * $m );
    }
}
