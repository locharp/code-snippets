class Solution
{

    public int missingNumber
    ( int[] nums )
    {
        HashSet< Integer > set1 =
            new HashSet<>();
        HashSet< Integer > set2 =
            new HashSet<>();
        set1.add( nums.length );
        
        for ( int i = 0; i < nums.length; i++ )
        {
            set1.add( i );
            set2.add( nums[i] );
        }

        set1.removeAll( set2 );
        int ans = 0;
        
        for ( Integer i : set1 )
        {
            ans = i;
        }

        return ans;
    }

}
