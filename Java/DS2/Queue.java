package DS2;

class Queue {
  private List list = new List();
  
  Queue() {
    list = new List();
  }

  Queue(List list) {
    this.list = list;
  }

  boolean isEmpty() {
    return list.isEmpty();
  }

  int getCount() {
    return list.getCount();
  }

  void enqueue(Object data) {
    list.addToTail(data);
  }

  Object next() {
    return list.tailData();
  }

  Object dequeue() {
    return list.removeFromHead();
  }

  public String toString() {
    return list.toString();
  }
}
