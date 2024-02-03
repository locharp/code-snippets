class Solution
{
    
    public String triangleType
    ( int[] nums )
    {
        Arrays.sort( nums );
        
        if ( nums[2] >= nums[0] + nums[1] )
        {
            return "none";
        }
        else if ( nums[0] == nums[1] )
        {
            if ( nums[1] == nums[2] )
            {
                return "equilateral";
            }
            else
            {
                return "isosceles";
            }
        }
        else if ( nums[1] == nums[2] )
        {
            return "isosceles";
        }
        else
        {
            return "scalene";
        }
    }
    
}
