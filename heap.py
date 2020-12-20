class Heap:
    def __init__(self, arr_data, min_heap = True):
        self.arr_data = arr_data
        self.compare_func = (lambda parent, child : parent > child) if min_heap else (lambda parent, child : parent < child)
        for index, _ in enumerate(self.arr_data):
            self._heap_up(index)

    def _heap_up(self, start_index):
        tmp_index = start_index
        while True:
            parent_index = int((tmp_index -1) / 2)
            if tmp_index == 0:
                break
            if self.compare_func(self.arr_data[parent_index], self.arr_data[tmp_index]):
                self.arr_data[parent_index], self.arr_data[tmp_index] = self.arr_data[tmp_index], self.arr_data[parent_index]
            else:
                break
            tmp_index = parent_index

    def push(self, val):
        self.arr_data.append(val)
        self._heap_up(len(self.arr_data) - 1)

    def pop(self):
        if len(self.arr_data) == 0:
            return (False, None)
        val = self.arr_data[0]
        self.arr_data[0] = self.arr_data[len(self.arr_data) - 1]
        self.arr_data.pop()
        self._heap_down()
        return (True, val)
    
    def _heap_down(self):
        total_len = len(self.arr_data)
        parent_index = 0
        while True:
            left_child_index = parent_index * 2 + 1
            right_child_index = parent_index * 2 + 2
            
            # left child and right child are None
            if left_child_index >= total_len:
                break
            # has left child and right child is None
            if left_child_index < total_len and right_child_index == total_len:
                if self.compare_func(self.arr_data[parent_index], self.arr_data[left_child_index]):
                    self.arr_data[left_child_index], self.arr_data[parent_index] = self.arr_data[parent_index], self.arr_data[left_child_index]
                    parent_index = left_child_index
                else:
                    break
            # has left child and has right child
            else:
                child_index = right_child_index if self.compare_func(self.arr_data[left_child_index], self.arr_data[right_child_index]) else left_child_index
                if self.compare_func(self.arr_data[parent_index], self.arr_data[child_index]):
                    self.arr_data[child_index], self.arr_data[parent_index] = self.arr_data[parent_index], self.arr_data[child_index]
                    parent_index = child_index
                else:
                    break

    def sort(self):
        result = []
        while len(self.arr_data) != 0:
            val = self.pop()
            result.append(val[1])
        return result
    
    def replace_root(self, val):
        if self.arr_data:
            self.arr_data[0] = val
            self._heap_down()
            return True
        else:
            return False

def find_max_m_elements(data_arr, m):
    total = len(data_arr)
    if total <= m:
        return data_arr
    else:
        min_heap = Heap(data_arr[:m])
        loop_indexs = range(m, total)
        for i in loop_indexs:
            if data_arr[i] > min_heap.arr_data[0]:
                min_heap.replace_root(data_arr[i])
        return min_heap.sort()

print(find_max_m_elements([1,2,3,4,9,6,7,8,9,100,101], 4))

import math

def determine_distance(point):
    x = point[0]
    y = point[1]
    return math.sqrt(x ** 2 + y ** 2)

def find_closest_points(points, m):
    max_heap = Heap(list(map(determine_distance, points[:m])), False)
    other_data = list(map(determine_distance, points[m:]))
    for val in other_data:
        if val < max_heap.arr_data[0]:
            max_heap.replace_root(val)
    return max_heap.sort()

print(find_closest_points([(0, 0), (1, 1), (2, 2), (3, 3)], 3))

class PriorityQueue:
    def __init__(self):
        self.min_heap = Heap([])
        self.size = 0
    
    def enqueue(self, val):
        self.min_heap.push(val)
        self.size += 1
    
    def dequeue(self):
        res = self.min_heap.pop()
        if res[0]:
            self.size -= 1
        return res
    
    def empty(self):
        return self.size == 0

# define a priority queue
pqueue = PriorityQueue()
pqueue.enqueue(10)
pqueue.enqueue(1)
pqueue.enqueue(7)
pqueue.enqueue(3)

while not pqueue.empty():
    res = pqueue.dequeue()
    print(res)

# define a min heap
minHeap = Heap([2,10,1,5,8,22])
print(minHeap.sort())

# define a max heap
maxHeap = Heap([2,10,1,5,8,22], False)
print(maxHeap.sort())