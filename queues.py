from node import Node

class Queue:
    def __init__(self,value):
        new_node = Node(value=value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            print('|')
            print('v')
            temp = temp.next
        print()

    def enqueue(self,value):
        new_node = Node(value=value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -= 1
        return temp