package DS2;

class List {
  private Node head, tail;
  private int count;

  boolean isEmpty() {
    return count == 0;
  }

  int getCount() {
    return count;
  }

  void addToHead(Object data) {
    if (count == 0)
      head = tail = new Node(data);
    else {
      head = new Node(data, head);
      head.next.prev = head;
    }
    count++;
  }

  void addToTail(Object data) {
    if (count == 0)
      head = tail = new Node(data);
    else
      tail = tail.next = new Node(tail, data);
    count++;
  }

  Object headData() {
    if (count == 0)
      throw new StructureEmptyError("List is empty.");
    else
      return head.data;
  }

  Object tailData() {
    if (count == 0)
      throw new StructureEmptyError("List is empty.");
    else
      return tail.data;
  }

  Object removeFromHead() {
    Object data = headData();
    if (count == 1)
      head = tail = null;
    else
      head = head.next;
    count--;
    return data;
  }

  Object removeFromTail() {
    Object data = tailData();
    if (count == 1)
      head = tail = null;
    else {
      tail = tail.prev;
      tail.next = null;
    }
    count--;
    return data;
  }

  public String toString() {
    if (count == 0)
      return "[]";    
    String s = "[" + head.data;
    Node curr = head.next;
    while (curr != null) {
      s += ", " + curr.data;
      curr = curr.next;
    }
    return s + ']';
  }
}
