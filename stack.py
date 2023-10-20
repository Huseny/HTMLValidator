# Name: Husen Yusuf
# ID No: UGR/7575/13
# -----------------------------------------

# Name: Amir Ahmedin
# ID No: UGR/4119/13
# -----------------------------------------
# Section 4

from LinkedList import LinkedList


class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push(self, element):
        self.list.pushFront(element)

    def pop(self):
        return self.list.popFront()

    def top(self):
        return self.list.topFront()

    def isEmpty(self):
        return self.list.isEmpty()

# We don't need the isFull method anymore since linked lists can have as many data as needed
# We have also used the pushFront and popFront methods of the LinkedList to define the pop and push 
# methods of the stack, but we can also use the pushBack and popBack methods of the LinkedList to achieve the
# same purpose.
