import java.util.HashMap;

public class AnagramMapping {
    public static int[] solution( int n, int[] a, int[] b ) {
        int answer[] = new int[n];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        
        for ( int i = 0; i < n; i++ ) {
            map.put( b[i], i );
        }

        for ( int i = 0; i < n; i++ ) {
            answer[i] = map.get( a[i] );
        }

        return answer;
    }

    public static void main( String[] args ) {
        int nums1[] = { 10, 20, 30, 40, 50 };
        int nums2[] = { 20, 10, 40, 50, 30 };
        int n = nums1.length;

        for ( int num : solution( n, nums1, nums2 ) ) {
            System.out.println( num );
        }
    }
}