package DS2;

class testDS2 {
  public static void main(String[] args) {
    List tmp = new List();
    System.out.println(tmp + "\nCount = " + tmp.getCount());
    tmp.addToHead(11);
    System.out.println(tmp + "\nCount = " + tmp.getCount());
    System.out.println(tmp.removeFromTail());
    System.out.println(tmp + "\nCount = " + tmp.getCount());
    tmp.addToTail(22);
    System.out.println(tmp + "\nCount = " + tmp.getCount());
    System.out.println(tmp.removeFromTail());
    System.out.println(tmp + "\nCount = " + tmp.getCount());
    tmp.addToTail(33);
    tmp.addToTail(44);
    tmp.addToHead(55);
    tmp.addToHead(66);
    System.out.println(tmp + "\nCount = " + tmp.getCount());
    System.out.println(tmp.removeFromHead());
    System.out.println(tmp + "\nCount = " + tmp.getCount());
    System.out.println(tmp.removeFromTail());
    System.out.println(tmp + "\nCount = " + tmp.getCount());
    
    Node t = new Node(new IntegerComparator());
    t.insert(10);
    t.insert(16);
    t.insert(4);
    t.insert(13);
    t.insert(8);
    t.insert(2);
    t.insert(8);
    t.insert(20);
    System.out.println();
    t.preorder();
    System.out.println();
    t.inorder();
    System.out.println();
    t.postorder();
    System.out.println();
    t.inorder_r();

    t = new Node(new CharacterComparator());
    t.insert('H');
    t.insert('h');
    t.insert('a');
    t.insert('i');
    t.insert('o');
    t.insert('p');
    t.insert('j');
    t.insert('m');
    System.out.println();
    t.preorder();
    System.out.println();
    t.inorder();
    System.out.println();
    t.postorder();
    System.out.println();
    t.inorder_r();
  }
}
