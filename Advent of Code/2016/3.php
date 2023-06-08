<?php

require_once( "../conn_aoc.php" );

$sql = "SELECT content FROM Year_2016 WHERE id = 3;";
$result = $conn->query( $sql );
$inputs = $result->fetchColumn();
$conn = NULL;
$inputs = explode( "\n", $inputs );

function is_valid( $sides )
{
    $max = max( $sides );
    $others = array_sum( $sides ) - $max;

    return ( $others > $max ) ? 1 : 0;
}

$count1 = 0;
$count2 = 0;

for ( $i = 0; $i < count( $inputs ); $i++ )
{
    $inputs[$i] = str_split( $inputs[$i], 6 );
    $inputs[$i] = array_map( "intval", $inputs[$i] );
    $count1 += is_valid( $inputs[$i] );
    
    if ( $i % 3 == 2 )
    {
        for ( $j = 0, $h = $i - 1, $g = $i - 2; $j < 3; $j++ )
        {
            $set = [ $inputs[$i][$j], $inputs[$h][$j], $inputs[$g][$j] ];

            $count2 += is_valid( $set );
        }
    }
}

print( "<h2>Day 3</h2><h3>Part 1</h3>" );
print( $count1 );
print( "<h3>Part 2</h3>" );
print( $count2 );

?>