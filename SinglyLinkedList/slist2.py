"""
Single linked list based on two pointer approach.

"""


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class slist:
    """
    singly linked list class
    """
    def __init__(self):
        self._first = None
        self._last = None

    def _build_a_node(self, i: int, append:bool=True):
        n = Node(val=i)
        # Handle empty list case
        if self._first is None and self._last is None:
            self._first = n
            self._last = n
        else:
            if append:
                self._last.next = n
                self._last = n
            else:
                n.next = self._first
                self._first = n

    def _find(self, x: int):
        nodes = [self._first, None]
        while nodes[0] != None:
            if nodes[0].val == x:
                return nodes
            nodes[1] = nodes[0]
            nodes[0] = nodes[0].next
        return nodes

    def append(self, i:int):
        self._build_a_node(i)

    def build_slist_from_list(self, a:list):
        for i in a:
            self.append(i)

    def find(self, x:int):
        nodes = self._find(x)
        if nodes[0]:
            return True
        else:
            return False

    def delete(self, x:int):
        nodes = self._find(x)
        # in case of node found
        if(nodes[0]):
            currentnode = nodes[0]
            previousnode = nodes[1]
            # list has only one element and that element is x
            if currentnode == self._first and currentnode == self._last and previousnode == None:
                self._first = None
                self._last = None
            # x at first position and being removed
            elif currentnode == self._first:
                self._first = currentnode.next
            # x at last position
            elif currentnode == self._last:
                previousnode.next = None
                self._last = previousnode
            # x is in between
            else:
                previousnode.next = currentnode.next

    def reverse(self):
        c = self._first
        self._last = self._first
        p = None
        while c != None:
            n = c.next
            c.next = p
            p = c
            c = n
        self._first = p

    def has_a_cycle(self):
        """
        find linked list has a cycle or not
        :return:
        """
        if self._first == None or self._first.next == None:
            return False
        ptr1 = self._first
        ptr2 = self._first.next
        while ptr1 != ptr2:
            if ptr2 == None or ptr2.next == None:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return True


    def find_mid_point(self):
        ptr1 = self._first
        ptr2 = self._first
        while(ptr2.next != None):
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
        return ptr1.val

    def __str__(self):
        s = ""
        n = self._first
        # in case slist is empty
        if n == None:
            s = s + "Null"

        # for other cases
        while n != None:
            s = s + str(n.val)
            if n.next is not None:
                s = s + "->"
            else:
                s = s + '->Null'
            n = n.next
        return s

    def __len__(self):
        l = 0
        n = self._first
        if not n:
            return l
        else:
            while n is not None:
                l +=1
                n = n.next
        return l


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 12, 6, 7, 8, 10, 10]
    s = slist()
    s.build_slist_from_list(a)
    print(s.has_a_cycle())
