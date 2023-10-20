# Name: Husen Yusuf
# ID No: UGR/7575/13
# -----------------------------------------

# Name: Amir Ahmedin
# ID No: UGR/4119/13
# -----------------------------------------
# Section 4

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pushFront(self, key):
        newNode = Node(key)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def topFront(self):
        if self.isEmpty():
            raise Exception ("List is empty")
        data = self.head.data
        return data

    def popFront(self):
        if self.isEmpty():
            raise Exception("No item to pop")
        firstElement = self.head
        self.head = self.head.next
        return firstElement.data

    def pushBack(self, item):
        node = Node(item)
        lastNode = self.tail
        lastNode.next = node
        self.tail = node

    def topBack(self):
        if self.isEmpty():
            raise Exception("List is  Empty")
        lastNode = self.tail
        return lastNode.data

    def popBack(self):
        if self.isEmpty():
            raise Exception("No item to pop")
        currentNode = self.head
        if currentNode == self.tail:
            self.head = None
            self.tail = None
            return currentNode.data
        while currentNode.next != self.tail:
            currentNode = currentNode.next
        lastNode = currentNode.next
        self.tail = currentNode
        return lastNode.data

    def erase(self, item):
        if self.isEmpty():
            raise Exception("No item to erase")
        prevItemNode = self.__searchPrevNode__(item)
        itemNode = prevItemNode.next
        prevItemNode.next = itemNode.next
        return itemNode.data

    def addBefore(self, key, item):
        if key == self.head.data:
            self.pushFront(item)
        else:
            itemNode = Node(item)
            keyNode = (self.__searchPrevNode__(key)).next
            prevNode = self.head
            while prevNode.next != keyNode and prevNode.next is not None:
                prevNode = prevNode.next
            if prevNode.next == keyNode:
                itemNode.next = keyNode
                prevNode.next = itemNode

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def find(self, item):
        if self.isEmpty():
            return False
        currentNode = self.head
        while currentNode.data != item and currentNode.next is not None:
            currentNode = currentNode.next
        if currentNode.data == item:
            return True
        return False

    def __searchPrevNode__(self, item):
        currentNode = self.head
        while currentNode.next.data != item and currentNode.next != self.tail:
            currentNode = currentNode.next

        if currentNode.next.data == item:
            return currentNode
        raise Exception("The referenced item " + str(item) + " not found")
