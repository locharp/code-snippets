function remove_char(string $s): string {
  // Write your code here
  return substr($s, 1, strlen($s) - 2);
function remove_char( string $s ): string
{
    return substr($s, 1, strlen($s) - 2);
}