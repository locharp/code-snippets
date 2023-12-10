function isVow( array $a )
{
    $vowels = [ 97, 101, 105, 111, 117 ];
    
    for ( $i = 0; $i < count( $a ); $i++ )
    {
        if ( in_array( $a[ $i ], $vowels ) )
        {
            $a[ $i ] = chr( $a[ $i ] );
        }
    }
    
    return $a;
}
