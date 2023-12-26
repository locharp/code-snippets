using System;

public class Sum
{
     public int GetSum(int a, int b)
     {
         if ( a > b )
         {
             int t = a;
             a = b;
             b = t;
         }
         
         int ans = b;
         
         for ( int i = a; i < b; i++ )
         {
             ans += i;
         }
         
         return ans;
     }
}
