<?php

require_once( "../conn_aoc.php" );

$sql = "SELECT content FROM Year_2016 WHERE id = 4;";
$result = $conn->query( $sql );
$conn = NULL;
$inputs = $result->fetchColumn();
$inputs = explode( "\n", $inputs );
$letters = range( "a", "z" );

function decrypt( $s, $id )
{
    global $letters;
    
    return implode( "", array_map( fn( $ch )  => $letters[(ord( $ch ) - 97 + $id ) % 26], str_split( $s ) ) );
}

$sum = 0;
$room = 0;

foreach ( $inputs as $input )
{
    $name = substr( $input, 0, -12 );
    $id = intval( substr( $input, -11, 3 ) );
    $checksum = substr( $input, -7, 5 );
    $object = substr( $input, 10, 6 );

    if ( strpos( decrypt( $object, $id ), "bject" ) )
    {
        $room = $id;
    }

    $chars = array();
    foreach ( str_split( $name ) as $ch )
    {
        if ( $ch == "-" )
        {
            continue;
        }
        elseif ( array_key_exists( $ch, $chars ) )
        {
            $chars[$ch]++;
        }
        else
        {
            $chars[$ch] = 1;
        }
    }

    arsort( $chars );
    $pass = array();
    $max = max( $chars );
    
    while ( count( $pass ) < 5 )
    {
        $tmp = array();
        
        foreach ( $chars as $ch => $c )
        {
            if ( $c > $max )
            {
                continue;
            }
            elseif ( $c == $max )
            {
                array_push( $tmp, $ch );
            }
            else
            {
                break;
            }
        }                

        sort( $tmp );
        array_push( $pass, ...$tmp );
            
        $max--;
    }

    for( $i = 0; $i < 5; $i++ )
    {
        if ( $pass[$i] != $checksum[$i] )
        {
            continue 2;
        }
    }

    $sum += $id;
}

print( "<h2>Day 4</h2><h3>Part 1</h3>" );
print( $sum );
print( "<h3>Part 2</h3>" );
print( $room );

?>