class StructureEmptyError(private val msg: String = "Structure is empty."): Error(msg) {}

class Node(var data: Int, var next: Node? = null) {}

class List(private var head: Node? = null, var tail: Node? = null, var nodeCount: Int = 0) {
  fun isEmpty(): Boolean = nodeCount == 0
  fun getCount() = nodeCount

  fun addToHead(data: Int) {
    if (nodeCount == 0) {      
      head = Node(data)
      tail = head
    } else {
      head = Node(data, head)
    }
    nodeCount++
  }

  fun addToTail(data: Int) {
    if (nodeCount == 0) {
      head = Node(data)
      tail = head
    } else {
      tail?.next = Node(data)
      tail = tail!!.next
    }
    nodeCount++
  }

  fun headData(): Int {
    if (nodeCount == 0)
      throw StructureEmptyError()
    return head!!.data
  }

  fun tailData(): Int {
    if (nodeCount == 0)
      throw StructureEmptyError()
    return tail!!.data
  }

  fun removeFromHead(): Int {
    val data = headData()
    if (nodeCount == 1) {
      head = null
      tail = null
    } else
      head = head!!.next
    nodeCount--
    return data
  }
  
  fun removeFromTail(): Int {
    val data = tailData()
    if (nodeCount == 1) {
      head == null
      tail = null
    } else {
      var curr = head
      while (curr!!.next != tail)
        curr = curr.next
      tail = curr
      tail!!.next = null
    }
    nodeCount--
    return data
  }

  override fun toString(): String {
    if (nodeCount == 0)
      return "[]"
    var s = "[" + head!!.data
    var curr = head?.next
    while(curr != null) {
      s += ", " + curr.data
      curr = curr.next
    }
    s += ']'
    return s
  }
}

class Stack(private val list: List = List()) {
  fun isEmpty() = list.isEmpty()
  fun getCount() = list.getCount()
  fun push(data: Int) = list.addToHead(data)
  fun pop() = list.removeFromHead()

  fun top(): Int {
    val data = list.removeFromHead()
    push(data)
    return data
  }

  override fun toString(): String = list.toString()
}

class Queue(private val list: List = List()) {
  fun isEmpty() = list.isEmpty()
  fun getCount() = list.getCount()
  fun enqueue(data: Int) = list.addToTail(data)
  fun next() = list.headData()
  fun dequeue() = list.removeFromHead()
  override fun toString(): String = list.toString()
}

fun main() {
  val tmp = Queue()
  tmp.enqueue(88)
  println("$tmp\nCount: ${tmp.getCount()}")
  println(tmp.next())
  println("$tmp\nCount: ${tmp.getCount()}")
  println(tmp.dequeue())
  println("$tmp\nCount: ${tmp.getCount()}")
  tmp.enqueue(11)
  tmp.enqueue(22)
  println(tmp.next())
  println("$tmp\nCount: ${tmp.getCount()}")
  tmp.enqueue(33)
  println("$tmp\nCount: ${tmp.getCount()}")
  println(tmp.dequeue())
  println("$tmp\nCount: ${tmp.getCount()}")
}