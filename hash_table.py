import hashlib
import singly_linked_list

def hash_function(key):
    return hashlib.md5(key.encode()).digest()

def index(storage, hash_code):
    return int.from_bytes(hash_code, 'big') & (len(storage) - 1)

def remove(storage, key, value):
    hash_code = hash_function(key)
    idx = index(storage, hash_code)
    removed_node = storage[idx].remove(key)
    return removed_node

# return 1 when insert, 0 when replace
def set(storage, key, value):
    hash_code = hash_function(key)
    idx = index(storage, hash_code)
    return storage[idx].insert(key, value)

def search(storage, key):
    hash_code = hash_function(key)
    idx = index(storage, hash_code)
    single_linked_list = storage[idx]
    return single_linked_list.find(key)

class HashTable:
    def __init__(self, number_of_buckets):
        self.number_of_entries = 0
        self.active_storage = [singly_linked_list.SinglyLinkedList() for i in range(number_of_buckets)]
        self.back_end_storage = None
    
    def _load_factor(self):
        return self.number_of_entries / len(self.active_storage)

    def __getitem__(self, key):
        result = search(self.active_storage, key)
        if result is None and self.back_end_storage is not None:
            result = search(self.back_end_storage, key)
        return result
    
    def __setitem__(self, key, value):
        should_rehash = self._load_factor() > 0.75
        count_of_added_entry = 0 # the final value will either be 0 or 1
        if should_rehash:
            count_of_added_entry = self._rehash(key, value)
        else:
            count_of_added_entry = set(self.active_storage, key, value)
        self.number_of_entries += count_of_added_entry

    def _rehash(self, key, value):
        from_storage = self.active_storage
        if self.back_end_storage is None:
            # first time to rehash
            self.back_end_storage = [singly_linked_list.SinglyLinkedList() for i in range(len(self.active_storage) * 2)]
            self.number_of_old_entries = self.number_of_entries
        to_storage = self.back_end_storage

        removed_node = remove(from_storage, key, value)
        if removed_node is not None:
            set(to_storage, removed_node.key, removed_node.value)
            self.number_of_old_entries -= 1
            if self.number_of_old_entries == 0:
                self.active_storage = self.back_end_storage
                self.back_end_storage = None
            return 0
        else:
            set(to_storage, key, value)
            return 1


if __name__ == '__main__':
    my_hash = HashTable(8)
    my_hash['abc'] = 1
    my_hash['abc1'] = 2
    print(my_hash['abc'])
    print(my_hash['abc1'])
