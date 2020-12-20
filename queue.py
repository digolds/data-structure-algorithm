import doubly_linked_list

class Queue:
    def __init__(self):
        self.doubly_linked_list = doubly_linked_list.DoublyLinkedList()
    
    def enqueue(self, val):
        self.doubly_linked_list.add_to_tail(val)
    
    def dequeue(self):
        return self.doubly_linked_list.remove_from_head()
    
    def empty(self):
        return self.doubly_linked_list.empty()

class DeQueue:
    def __init__(self):
        self.doubly_linked_list = doubly_linked_list.DoublyLinkedList()
    
    def push_back(self, val):
        self.doubly_linked_list.add_to_tail(val)

    def push_front(self, val):
        self.doubly_linked_list.add_to_head(val)

    def pop_back(self):
        return self.doubly_linked_list.remove_from_tail()

    def pop_front(self):
        return self.doubly_linked_list.remove_from_head()
    
    def empty(self):
        return self.doubly_linked_list.empty()

if __name__ == '__main__':
    print('simple queue')
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(19)
    queue.enqueue(18)
    while not queue.empty():
        print(queue.dequeue())
    
    print('double ended queue')
    my_deque = DeQueue()
    my_deque.push_back(1)
    my_deque.push_front(21)
    my_deque.push_front(110)
    my_deque.push_back(39)
    my_deque.push_back(99)

    res = []
    res.append(my_deque.pop_front())
    res.append(my_deque.pop_front())
    res.append(my_deque.pop_front())
    res.append(my_deque.pop_front())
    res.append(my_deque.pop_front())
    print(res)