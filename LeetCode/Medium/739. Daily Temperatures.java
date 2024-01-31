import java.util.AbstractMap.SimpleImmutableEntry;

class Solution
{
    
    public int[] dailyTemperatures
    ( int[] temperatures )
    {
        int n = temperatures.length;
        int[] ans = new int[n];
        Stack< SimpleImmutableEntry< Integer, Integer > > stack =
            new Stack<>();
            
        for ( int i = 0; i < n; i++ )
        {
            while ( !stack.isEmpty()
                 && stack.peek().getValue() < temperatures[i] )
            {
                int j = stack.pop().getKey();
                ans[j] = i - j;
            }
            
            stack.push( new SimpleImmutableEntry<>( i, temperatures[i] ) );
        }
        
        return ans;
    }
    
}
