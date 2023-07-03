class SnapshotArray
{
    private $arr;
    private $snapshots;
    private $snap_id;
    /**
     * @param Integer $length
     */
    function __construct($length)
    {
        $this->snap_id = 0;
    }
  
    /**
     * @param Integer $index
     * @param Integer $val
     * @return NULL
     */
    function set($index, $val)
    {
        $this->arr[$index] = $val;
    }
  
    /**
     * @return Integer
     */
    function snap()
    {
        $this->snapshots[$this->snap_id] = $this->arr;
        
        return $this->snap_id++;
    }
  
    /**
     * @param Integer $index
     * @param Integer $snap_id
     * @return Integer
     */
    function get($index, $snap_id)
    {
        if ( isset( $this->snapshots[$snap_id][$index] ) )
        {
            return $this->snapshots[$snap_id][$index];
        }
        else
        {
            return 0;
        }
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * $obj = SnapshotArray($length);
 * $obj->set($index, $val);
 * $ret_2 = $obj->snap();
 * $ret_3 = $obj->get($index, $snap_id);
 */