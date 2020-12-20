class DoublyLinkedListNode:
    def __init__(self, val):
        self.pre = None
        self.next = None
        self.value = val

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_tail(self, val):
        new_node = DoublyLinkedListNode(val)
        if self.empty():
            self.tail = self.head = new_node
        else:
            new_node.pre = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
    
    def remove_from_tail(self):
        val = self.tail.value
        self.count -= 1
        if self.empty():
            self.head = self.tail = None
        else:
            self.tail.pre.next = None
        return val
    
    def add_to_head(self, val):
        new_node = DoublyLinkedListNode(val)
        if self.empty():
            self.tail = self.head = new_node
        else:
            new_node.next = self.head
            self.head.pre = new_node
            self.head = new_node
        self.count += 1

    def remove_from_head(self):
        val = self.head.value
        self.head = self.head.next
        self.count -= 1
        if self.empty():
            self.tail = None
        else:
            self.head.pre = None
        return val

    def empty(self):
        return self.count == 0

    def print_all(self, reverse = False):
        current_node = self.head
        next_node = lambda x : x.next
        if reverse:
            current_node = self.tail
            next_node = lambda x : x.pre
        while current_node:
            print(current_node.value)
            current_node = next_node(current_node)

if __name__ == "__main__":
    double_linked_list = DoublyLinkedList()
    double_linked_list.add_to_tail(1)
    double_linked_list.add_to_tail(10)
    double_linked_list.add_to_tail(90)
    double_linked_list.add_to_tail(100)
    double_linked_list.add_to_tail(2)
    print('traverse from head')
    double_linked_list.print_all()
    print('traverse from tail')
    double_linked_list.print_all(True)