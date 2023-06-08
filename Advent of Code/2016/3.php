<?php

require_once( "../conn_aoc.php" );

$sql = "SELECT content FROM Year_2016 WHERE id = 3;";
$result = $conn->qusry( $sql );
$inputs = $result->fetchColumn();
$conn = NULL;
$triangles = array();

foreach ( $inputs as $input )
{
    array_push( $triangles, array_map( "int", explode( input ) ) );
}

print_r( $triangles );

?>