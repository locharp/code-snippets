import java.util.*;

public class SetMatrixZeros {
    public static void SetZeros(int matrix[][]) {
        Set<Integer> rows = new HashSet<>();
        Set<Integer> cols = new HashSet<>();
        int m = matrix.length;
        int n = matrix[0].length;

        for ( int = 0; i < m; i++ ) {
            for ( int j = 0; j < n; j++ ) {
                if ( matrix[i][j] == 0 ) {
                    rows.add( i );
                    cols.add( j );
                }
            }
        }
        
        for ( int c : cols ) {
            for ( int i = 0; i < m; i++ ) {
                matrix[i][c] = 0;
            }
        }

        for ( int r : rows ) {
            Arrays.fill( matrix[r], 0 );
        }
    }
}