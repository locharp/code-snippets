class Solution
{

    /**
     * @param Integer $num
     * @return Integer
     */
    function numberOfSteps( $num )
    {
        $steps = 0;
        while ($num > 0) {
            if ($num % 2 == 0) {
                $num /= 2;
            } else {
                $num--;
            }
            $steps++;
        }
        
        return $steps;
    }
}