function solution( $inputString )
{
    $len = strlen( $inputString ) - 1;
    
    for ( $i = 0; $i < $len / 2; $i++ )
    {
        if ( $inputString[$i] != $inputString[$len - $i])
        {
            return FALSE;
        }
    }
    
    return TRUE;
}
