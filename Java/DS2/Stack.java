package DS2;

class Stack {
  private List list;

  Stack() {
    list = new List();
  }

  Stack(List list) {
    this.list = list;
  }

  boolean isEmpty() {
    return list.isEmpty();
  }

  int getCount() {
    return list.getCount();
  }

  void push(Object data) {
    list.addToHead(data);
  }

  Object top() {
    return list.headData();
  }

  Object pop() {
    return list.removeFromHead();
  }

  public String toString() {
    return list.toString();
  }
}
