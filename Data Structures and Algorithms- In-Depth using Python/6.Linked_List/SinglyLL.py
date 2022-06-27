from requests import head


class _Node:
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next
    

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    # Returns length of Linked List
    def __len__(self):
        return self._size
    # Returns True if List is empty
    def isempty(self):
        return self._size == 0
    # Inserting element at end of List 
    def addLast(self, ele):
        newest = _Node(ele, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    # Displays every element
    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()
    # Search in Linked List
    def search(self, Key):
        p = self._head
        index = 0
        while p:
            if p._element == Key:
                return index
            p = p._next
            index += 1
        return -1
    # Inserting element at beginning of List
    def addFirst(self,ele):
        newest = _Node(ele, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else:
            newest._next = self._head
            self._head = newest
        self._size += 1
    # Inserting element at any position of List
    def addAny(self,ele, position):
        newest = _Node(ele, None)
        p = self._head
        i = 1
        while i<position-1:
            p = p._next
            i +=1
        newest._next = p._next
        p._next = newest
        self._size += 1
    # Deleting element at beginning of List
    def removeFirst(self):
        if self.isempty():
            print('List is empty')
            return
        ele = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.isempty():
            self._tail = None
        return ele
    # Deleting element at ending of List
    def removeLast(self):
        if self.isempty():
            print('List is empty')
            return
        p = self._head
        i = 1
        while i<len(self)-1:
            p = p._next
            i +=1
        self._tail = p
        p = p._next
        ele = p._element
        self._tail._next = None
        self._size -= 1
        return ele
    # Deleting element at any position of List
    def removeAny(self,position):
        p = self._head
        i = 1
        while i<position-1:
            p = p._next
            i +=1
        ele = p._next._element
        p._next = p._next._next
        self._size -= 1
        return ele

L =LinkedList()
L.addLast(7)
L.addFirst(6)
L.addLast(1)
L.addFirst(4)
L.addLast(12)
L.addFirst(2)
L.addAny(9,4)
L.display()

ele = L.removeLast()
print('Last element removed:', ele)
ele = L.removeFirst()
print('First element removed:', ele)
ele = L.removeAny(3)
print('3rd element removed:', ele)
L.display()
idx = L.search(6)
print('Index of target Key:', idx)