class Solution
{
    public List< List<Integer> > findMatrix( int[] nums )
    {
        int[] freq = new int[ nums.length + 1 ];
        ArrayList< List<Integer> > ans = new ArrayList<>();
        
        for ( int num : nums )
        {
            if ( freq[num] >= ans.size() )
            {
                ans.add( new ArrayList<>() );
            }

            ans.get( freq[num]++ ).add( num );
        }

        return ans;
    }
}
