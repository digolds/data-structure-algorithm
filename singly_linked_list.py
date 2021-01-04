
class SinglyLinkedListNode:
    def __init__(self, key, val):
        self.next = None
        self.key = key
        self.value = val

    def __str__(self):
        return f'{self.key},{self.value}'

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add_to_tail(self, key, val):
        new_node = SinglyLinkedListNode(key, val)
        if self.count == 0:
            self.tail = self.head = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def remove_from_head(self):
        head = self.head
        self.head = self.head.next
        self.count -= 1
        if self.empty():
            self.tail = None
        return head

    def find(self, key):
        current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                return current_node
            current_node = current_node.next
        return None

    def insert(self, key, value):
        node = self.find(key)
        if node is None:
            self.add_to_tail(key, value)
            return 1
        else:
            node.value = value
            return 0

    def remove(self, key):
        previous_node = current_node = self.head
        while current_node is not None:
            if current_node.key == key:
                if previous_node == current_node:
                    return self.remove_from_head()
                else:
                    previous_node.next = current_node.next
                    current_node.next = None
                    return current_node
            previous_node = current_node
            current_node = current_node.next
        return None

    def empty(self):
        return self.count == 0

    def print_all(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next