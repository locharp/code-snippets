class Solution
{

    int[] nums;
    int i;
    int j;



    void f()
    {
        i = nums[i];
        j = nums[ nums[j] ];
        
        if ( i != j )
        {
            f();
        }
        else
        {
            i = 0;
            g();
        }
    }



    void g()
    {
        if ( i != j )
        {
            i = nums[i];
            j = nums[j];
            g();
        }
    }



    public int findDuplicate( int[] nums )
    {
        this.nums = nums;
        f();

        return i;
    }

}
