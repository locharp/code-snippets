<?php

require_once( "../conn_aoc.php" );

$sql = "SELECT content FROM Year_2016 WHERE id = 2;";
$result = $conn->query( $sql );
$inputs = $result->fetchColumn();
$conn = NULL;
$inputs = explode( "\n", $inputs );

print( "<h2>Day 2</h2><h3>Part 1</h3>" );

$keypad1 = array( array( 1, 2, 3 ), array( 4, 5, 6 ), array( 7, 8, 9 ) );
$r = 1;
$c = 1;

foreach ( $inputs as $input )
{
    for ( $i = 0; $i < strlen( $input ); $i++ )
    {
        switch ( $input[$i] )
        {
        case "U":
            if ( $r > 0 )
            {
                $r--;
            }
            break;
            
        case "D":
            if ( $r < 2 )
            {
                $r++;
            }
            break;
            
        case "L":
            if ( $c > 0 )
            {
                $c--;
            }
            break;
            
        case "R":
            if ( $c < 2 )
            {
                $c++;
            }
            break;
            
        default:
            break;
        }
    }
    print( $keypad1[$r][$c] );
}


// Part 2
print( "<h3>Part 2</h3>" );

$keypad2 = array(
    array ( 0, 0, 0, 0, 0, 0, 0 ),
    array ( 0, 0, 0, 1, 0, 0, 0 ),
    array ( 0, 0, 2, 3, 4, 0, 0 ),
    array ( 0, 5, 6, 7, 8, 9, 0 ),
    array ( 0, 0, "A", "B","C", 0, 0 ),
    array ( 0, 0, 0, "D", 0, 0, 0 ),
    array ( 0, 0, 0, 0, 0, 0, 0)
);
$keys = array( 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D" );

$r = 3;
$c = 1;

foreach ( $inputs as $input )
{
    for ($i = 0; $i < strlen( $input ); $i++ )
    {
        $r2 = $r;
        $c2 = $c;
        
        switch ( $input[$i] )
        {
        case "U":
            $r--;
            break;
                
        case "D":
            $r++;
            break;

        case "L":
            $c--;
            break;

        case "R":
            $c++;
            break;

        default:
            break;
        }

        if ( !in_array( $keypad2[$r][$c], $keys, TRUE ) )
        {
            $r = $r2;
            $c = $c2;
        }
    }

    print( $keypad2[$r][$c] );
}

?>