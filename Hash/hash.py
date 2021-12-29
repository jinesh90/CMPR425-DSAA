"""
implement hash by using singly linked list
"""

from slist import slist


class Hash:
    """
    hash implementation for python
    """
    def __init__(self, size):
        """
        initialized with size of dict
        :param size:
        """
        self._table_size = size
        self._size = 0
        self._hash = []
        for i in range(self._table_size):
            x = self._hash.append(slist())

    def insert(self, key):
        """
        insert key to  hash
        :param key:
        :return:
        """
        x = self._hash_function(key)
        self._hash[x].append(key)
        self._increment_size()

    def find(self, key):
        """
        find the key from hash
        :param key:
        :return:
        """
        x = self._hash_function(key)
        f = self._hash[x].find(key)
        return f

    def delete(self, key):
        """
        delete the key from hash
        :param key:
        :return:
        """
        x = self._hash_function(key)
        a = self._hash[x].delete(key)
        self._decrement_size()

    def _hash_function(self, key):
        """
        simple hash function for
        :param key:
        :return:
        """
        return key % (self._table_size)

    def _increment_size(self):
        self._size += 1

    def _decrement_size(self):
        self._size -= 1

    def __len__(self):
        return self._size


if __name__ == '__main__':
    h = Hash(10)
    h.insert(23)
    h.insert(34)
    h.insert(43)
    print(h.find(43))
    h.delete(43)
    print(h.find(43))
    print(len(h))




