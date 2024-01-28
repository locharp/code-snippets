class Solution
{
  
    public int countKeyChanges( String s )
    {
        int ans = -1;
        char last = ' ';
        
        for ( char ch : s.toLowerCase().toCharArray() )
        {
            if ( ch != last )
            {
                last = ch;
                ans ++;
            }
        }
        
        return ans;
    }
  
}
