<?php




function vertMirror( $s )
{
    $a = explode( "\n", $s );
    $n = count( $a );
    
    for ( $i = 0; $i < $n; $i++ )
    {
        $a[$i] = strrev( $a[$i] );
    }
    
    return join( "\n", $a );
}



function horMirror( $s )
{
    $a = explode( "\n", $s );
    $a = array_reverse( $a );
    
    return join( "\n", $a );
}



function oper( $fct, $s )
{
    return $fct( $s );
}



?>
