<?php

require_once("../conn_aoc.php");

$sql = "SELECT content FROM Year_2016 WHERE id = 1;";
$result = $conn->query($sql);
$text = $result->fetchColumn();
$conn = NULL;
$map = array_fill(0, 2000, array_fill(0, 2000, FALSE));

$face = "N";
$n = 1000;
$e = 1000;
$s = 0;
$w = 0;
$n2 = 0;
$e2 = 0;
$map[1000][1000] = TRUE;
$found = FALSE;

foreach (explode(', ', $text) as $inputs)
{
    switch ($face)
    {
    case "N":
        if ($inputs[0] == "L")
        {
            $face = "W";
            $s = 0;
            $w = 1;
        }
        else
        {
            $face = "E";
            $s = 0;
            $w = -1;
        }
        break;
        
    case "E":
        if ($inputs[0] == "L")
        {
            $face = "N";
            $s = -1;
            $w = 0;
        }
        else
        {
            $face = "S";
            $s = 1;
            $w = 0;
        }
        break;
        
    case "S":
        if ($inputs[0] == "L")
        {
            $face = "E";
            $s = 0;
            $w = -1;
        }
        else
        {
            $face = "W";
            $s = 0;
            $w = 1;
        }
        break;
        
    case "W":
        if ($inputs[0] == "L")
        {
            $face = "S";
            $s = 1;
            $w = 0;
        }
        else
        {
            $face = "N";
            $s = -1;
            $w = 0;
        }
        break;
    }

    for ($i = 0; $i < intval(substr($inputs, 1)); $i++)
    {
        $n -= $s;
        $e -= $w;
        if ($map[$e][$n])
        {
            if (!$found)
            {
                $n2 = $n;
                $e2 = $e;
                $found = TRUE;
            }
        }
        else
        {
            $map[$e][$n] = TRUE;
        }
    }
}

print("<h2>Day 1</h2><h3>Part 1</h3>");
print("Final Location = (" . $n . ", " . $e . ")<br />");
$distance = abs($n - 1000) + abs($e - 1000);
print("Distance = " . $distance . "<br /><br />");

print("<h3>Part 2</h3>");
print("Easter Bunny Headquarter Location = (" . $n2 . ", " . $e2 . ")<br />");
$distance2 = abs($n2 - 1000) + abs($e2 - 1000);
print("Distance 2 = " . $distance2 . "<br />");

?>