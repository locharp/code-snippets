public class Solution 
{

	public static String addBinaryString( String a, String b, int n, int m )
	{
		if ( n < m )
        {
            String s = a;
            a = b;
            b = s;
            int t = n;
            n = m;
            m = t;
        }

        StringBuilder ans = new StringBuilder();
        int i = 1;
        int c = 0;
        
        for ( ; i <= m; i++ )
        {
            c += a.charAt( n - i ) - '0' + b.charAt( m - i ) - '0';
            ans.append( c % 2 );
            c /= 2;
        }

        for ( ; i <= n; i++ )
        {
            c += a.charAt( n - i ) - '0';
            ans.append( c % 2 );
            c /= 2;
        }

        if ( c > 0 )
        {
            ans.append( c );
        }
        
        ans.reverse();

        return ans.toString();
	}
}
