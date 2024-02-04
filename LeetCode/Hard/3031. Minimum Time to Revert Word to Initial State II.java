class Solution
{
    
    public int minimumTimeToInitialState
    ( String word, int k )
    {
        int ans = 1;
        int i = k;
        
        while ( !word.startsWith( word.substring( i ) ) )
        {
            i += k;
            ans++;
            
            if ( i >= word.length() )
            {
                break;
            }
        }
        
        return ans;
    }
    
}
