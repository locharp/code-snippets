class Node:
    
    def __init__( self, val, next = None ):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__( self ):
        self.head = None
        self.size = 0

    def get( self, index: int ) -> int:
        if index >= self.size:
            return - 1
        
        i = 0
        curr = self.head
        
        while i < index:
            curr = curr.next
            i += 1
            
        return curr.val

    def addAtHead( self, val: int ) -> None:
        self.head = Node( val, self.head )
        self.size += 1

    def addAtTail( self, val: int ) -> None:
        if self.size == 0:
            self.head = Node( val )
            self.size += 1
            return
        
        curr = self.head
        
        while curr.next != None:
            curr = curr.next
            
        curr.next = Node( val )
        self.size += 1
        
    def addAtIndex( self, index: int, val: int ) -> None:
        if index > self.size:
            return
        elif index == 0:
            self.head = Node( val, self.head )
            self.size += 1
            return
        
        i = 1
        curr = self.head
        
        while i < index:
            curr = curr.next
            i += 1
            
        curr.next = Node( val, curr.next )
        self.size += 1

    def deleteAtIndex( self, index: int ) -> None:
        if index >= self.size:
            return
        elif index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        
        i = 1
        curr = self.head
        
        while i < index:
            curr = curr.next
            i += 1
            
        curr.next = curr.next.next
        self.size -= 1