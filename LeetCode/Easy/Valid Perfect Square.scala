object Solution
{
    def isPerfectSquare( num: Int ): Boolean =
    {
        val n = num.toLong
        var i = 1L
        var j = n
        
        while ( i <= j )
        {
            val m = ( i + j ) / 2
            val k = m * m
            
            if ( k > num )
            {
                j = m - 1
            }
            else if ( k < num )
            {
                i = m + 1
            }
            else
            {
                return true
            }
        }
        
        return false
    }
}
