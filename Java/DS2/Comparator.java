package DS2;

interface Comparator {
  boolean isEqual(Object obj1, Object obj2);
  boolean isGreaterThan(Object obj1, Object obj2);
  boolean isGreaterThanOrEqual(Object obj1, Object obj2);
  boolean isLessThan(Object obj1, Object obj2);
  boolean isLessThanOrEqual(Object obj1, Object obj2);
}

class IntegerComparator implements Comparator{
  public boolean isEqual(Object obj1, Object obj2) {
    return (Integer)obj1 == (Integer)obj2;
  }
  
  public boolean isGreaterThan(Object obj1, Object obj2) {
    return (Integer)obj1 > (Integer)obj2;
  }
  
  public boolean isGreaterThanOrEqual(Object obj1, Object obj2) {
    return (Integer)obj1 >= (Integer)obj2;
  }
  
  public boolean isLessThan(Object obj1, Object obj2) {
    return (Integer)obj1 < (Integer)obj2;
  }
  
  public boolean isLessThanOrEqual(Object obj1, Object obj2) {
    return (Integer)obj1 <= (Integer)obj2;
  }
}

class CharacterComparator implements Comparator{
  public boolean isEqual(Object obj1, Object obj2) {
    return (Character)obj1 == (Character)obj2;
  }
  
  public boolean isGreaterThan(Object obj1, Object obj2) {
    return (Character)obj1 > (Character)obj2;
  }
  
  public boolean isGreaterThanOrEqual(Object obj1, Object obj2) {
    return (Character)obj1 >= (Character)obj2;
  }
  
  public boolean isLessThan(Object obj1, Object obj2) {
    return (Character)obj1 < (Character)obj2;
  }
  
  public boolean isLessThanOrEqual(Object obj1, Object obj2) {
    return (Character)obj1 <= (Character)obj2;
  }
}

class StringComparator implements Comparator{
  public boolean isEqual(Object obj1, Object obj2) {
    return ((String)obj1).compareTo((String)obj2) == 0;
  }
  
  public boolean isGreaterThan(Object obj1, Object obj2) {
    return ((String)obj1).compareTo((String)obj2) > 0;
  }
  
  public boolean isGreaterThanOrEqual(Object obj1, Object obj2) {
    return ((String)obj1).compareTo((String)obj2) >= 0;
  }
  
  public boolean isLessThan(Object obj1, Object obj2) {
    return ((String)obj1).compareTo((String)obj2) < 0;
  }
  
  public boolean isLessThanOrEqual(Object obj1, Object obj2) {
    return ((String)obj1).compareTo((String)obj2) <= 0;
  }
}
