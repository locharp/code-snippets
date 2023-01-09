package DS2;

class Node {
  Object data;
  Node prev, next;
  Comparator comparator;

  Node() {}
  
  Node(Object data) {
    this.data = data;
  }

  Node(Node prev, Object data) {
    this.prev = prev;
    this.data = data;
  }

  Node(Object data, Node next) {
    this.data = data;
    this.next = next;
  }

  Node(Node prev, Object data, Node next) {
    this.prev = prev;
    this.data = data;
    this.next = next;
  }

  Node(Comparator comparator) {
    this.comparator = comparator;
  }

  Node(Object data, Comparator comparator) {
    this.data = data;
    this.comparator = comparator;
  }

  void insert(Object data) {
    if (this.data == null)
      this.data = data;
    else if (comparator.isLessThan(data, this.data))
      if (prev == null)
        prev = new Node(data, comparator);
      else
        prev.insert(data);
    else
      if (next == null)
        next = new Node(data, comparator);
      else
        next.insert(data);
  }

  void preorder() {
    System.out.print(data + " ");
    if (prev != null)
      prev.preorder();
    if (next != null)
      next.preorder();
  }

  void inorder() {
    if (prev != null)
      prev.inorder();
    System.out.print(data + " ");
    if (next != null)
      next.inorder();
  }

  void postorder() {
    if (prev != null)
      prev.postorder();
    if (next != null)
      next.postorder();
    System.out.print(data + " ");
  }
  
  void inorder_r() {
    if (next != null)
      next.inorder_r();
    System.out.print(data + " ");
    if (prev != null)
      prev.inorder_r();
  }
}
