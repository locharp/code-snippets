using System;

public class Kata
{
    public static int[] Get_size( int w,int h,int d )
    {
        int area = w * 2 * h;
        area += h * 2 * d;
        area += d * 2 * w;
        int volume = w * h * d;
        int[] ans = new int[] { area, volume };
        
        return ans;
    }
}
