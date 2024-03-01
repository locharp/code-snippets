class Solution
{

    public String maximumOddBinaryNumber
    ( String s )
    {
        int one = 0;

        for ( char ch : s.toCharArray() )
        {
            if ( ch == '1' )
            {
                one++;
            }
        }
        
        return "1".repeat(one - 1 ) + "0".repeat( s.length() - one ) + "1";
    }

}
