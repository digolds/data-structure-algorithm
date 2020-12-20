class SinglyLinkedListNode:
    def __init__(self, val):
        self.next = None
        self.value = val

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_tail(self, val):
        new_node = SinglyLinkedListNode(val)
        if self.count == 0:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def remove_from_head(self):
        val = self.head.value
        self.head = self.head.next
        self.count -= 1
        if self.empty():
            self.tail = None
        return val

    def empty(self):
        return self.count == 0
    
    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

single_linked_list = SinglyLinkedList()
single_linked_list.add_to_tail(1)
single_linked_list.add_to_tail(10)
single_linked_list.add_to_tail(90)
single_linked_list.add_to_tail(100)
single_linked_list.add_to_tail(2)

single_linked_list.print_all()