<?php

function is_consecutive( $p, $q )
{
    return $p + 1 == $q;
}

function summaryRanges($nums)
{
    $ranges = [];
    $len = count( $nums ) - 1;
    
    for ( $i = 0; $i <= $len; $i++ )
    {
            
        while ( $i < $len && !is_consecutive( $nums[$i], $nums[$i + 1] ) )
        {
            $ranges[] = strval( $nums[$i++] );
        }
        
        if ( $i < $len )
        {
            $start = $nums[$i++];
        }
        else
        {
            $ranges[] = strval( $nums[$i] );
            break;
        }
            
        while ( $i < $len && is_consecutive( $nums[$i], $nums[$i + 1] ) )
        {
            $i++;
        }
            
        $ranges[] = "$start->$nums[$i]";
    }
        
    return $ranges;
}

?>