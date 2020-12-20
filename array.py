class Array:
    def __init__(self, capacity=10):
        self.logical_size = 0
        self.capacity = capacity
        self.data = [0] * capacity

    def append(self, val):
        if self.logical_size == self.capacity:
            alloc_capacity = 2 * len(self.data)
            self.data = self.data + [0] * alloc_capacity
            self.capacity += alloc_capacity
        self.data[self.logical_size] = val
        self.logical_size += 1
    
    def pop(self):
        if self.logical_size == 0:
            return None
        else:
            res = self.data[self.logical_size - 1]
            self.logical_size -= 1
            return res
    
    def index(self, i):
        if i < self.logical_size:
            return self.data[i]
        else:
            return None
    
    def print(self):
        print(self.data[:self.logical_size])

one_dim_arr = Array()
one_dim_arr.append(10)
one_dim_arr.append(5)
one_dim_arr.append(106)
one_dim_arr.append(69)
one_dim_arr.pop()
one_dim_arr.append(12)

one_dim_arr.print()