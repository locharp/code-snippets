class Solution
{
    
    public int returnToBoundaryCount
    ( int[] nums )
    {
        int ans = 0;
        int curr = 0;
        
        for ( int num : nums )
        {
            curr += num;
            
            if ( curr == 0 )
            {
                ans++;
            }
        }
        
        return ans;
    }
}
