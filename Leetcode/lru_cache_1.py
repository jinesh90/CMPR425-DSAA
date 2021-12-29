"""
LRU cache by using python inbuilt data structure. Leetcode 146
"""

from collections import OrderedDict



class LRUCache(OrderedDict):
    """
    LRU class with order dict
    """
    def __init__(self, capacity):
        """
        set capacity as int
        :param capacity:
        """
        super().__init__()
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)

lru = LRUCache(5)
lru.put("A", 1)
lru.put("B", 2)
lru.put("C",3)
lru.put("D",4)
lru.put("E", 5)
print(lru.get("A"))
lru.put("F", 6)
print(lru)
print(lru.get("C"))
print(lru)
