import java.util.* ;
import java.io.*;

public class NinjaSubequence {
    static boolean isRegular( String s ) {
        char first = s.charAt( 0 );
        
        if ( first == ')' || s.charAt( s.length() - 1 ) == '(' ) {
            return false;
        }

        Stack<Character> stack = new Stack<>();
        stack.push( first );

        for ( char ch : s.substring( 1 ).toCharArray() ) {
            if ( ch == ')' ) {
                if ( stack.isEmpty() || stack.peek() != '(' ) {
                    return false;
                } else {
                    stack.pop();
                }
            } else {
                stack.push( ch );
            }
        }

        return stack.isEmpty();
    }

    public static String ninjaSubsequence( int n,String s, int k ) {
        if ( k > n ) {
            return "-1";
        }
        
        if ( !isRegular( s ) ) {
            if ( k > 1 ) {
                return "-1";
            } else {
                return s;
            }
        }
    
        for ( int i = 0; i < n; i++ ) {
            int j = i;

            while ( j < n ) {
                if ( s.charAt( i ) != s.charAt( j ) ) {
                    break;
                }

                j++;
            }

            if ( j < n && s.charAt( j ) == ')' ) {
                k--;

                if ( k == 0 ) {
                    return s.substring( 0, j ) + s.substring( j + 1 );
                }
            }

            i = j - 1;
        }

        for ( int i = n - 1; i >= 0; i-- ) {
            int j = i;

            while ( j >= 0 ) {
                if ( s.charAt( i ) != s.charAt( j ) ) {
                    break;
                }

                j--;
            }

            if ( j >= 0 && s.charAt( j ) == '(' ) {
                k--;

                if ( k == 0 ) {
                    return s.substring( 0, j ) + s.substring( j + 1 );
                }
            }
      
            i = j + 1;
        }

        return "-1";
    }

    public static void main(String[] args ) {
        String s = "()))";
        int len = s.length();
        
        System.out.println( ninjaSubsequence( len, s, 5 ) );
    }
}