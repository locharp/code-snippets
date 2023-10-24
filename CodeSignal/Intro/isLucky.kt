fun solution( n: Int ): Boolean
{
    val arr = n.toString().toCharArray().map{ it.toInt() }
    val len = arr.size
    val mid = len / 2
    
    return arr.slice( 0 until mid ).sum() == arr.slice( mid until len ).sum()
}
