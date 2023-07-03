class Solution
{

    /**
     * @param Integer $n
     * @return String[]
     */
    function fizzBuzz( $n )
    {
        $answer = [];
        
        for ( $i = 1; $i <= $n; $i++ )
        {
            if ( $i % 3 == 0 )
            {
                if ( $i % 5 == 0 )
                {
                    $answer[] = "FizzBuzz";
                }
                else
                {
                    $answer[] = "Fizz";
                }
            }
            else if ( $i % 5 == 0 )
            {
                $answer[] = "Buzz";
            }
            else
            {
                $answer[] = strval($i);
            }
        }
        
        return $answer;
    }
}