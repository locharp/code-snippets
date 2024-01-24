public class Solution
{
    
    int[] ans = [ -1, -1 ];
    int[] nums;
    int i, j, k, n, t;
    
    
    
    void f()
    {
        if ( i >= j )
        {
            if ( i < n && nums[i] == t )
            {
                 ans[0] = i;
            }
            
            return;
        }
        
        k = i + ( j - i ) / 2;
        
        if ( nums[k] < t )
        {
            i = k + 1;
            f();
        }
        else
        {
            j = k;
            f();
        }
    }
    
    
    
    void g()
    {
        if ( i == n )
        {
            ans[1] = i - 1;
            
            return;
        }
        
        k = i + ( n - i ) / 2;
        
        if ( nums[k] > t )
        {
            n = k;
            g();
        }
        else
        {
            i = k + 1;
            g();
        }
    }
    
    
    
    public int[] SearchRange( int[] nums, int target )
    {
        this.nums = nums;
        t = target;
        n = nums.Length;
        j = n - 1;
        f();
        
        if ( ans[0] >= 0 )
        {
            g();
        }
        
        return ans;
    }
    
}
