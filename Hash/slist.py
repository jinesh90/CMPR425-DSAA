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

    def build_slist_from_list(self, a):
        """
        building a singly linked list from a given list
        :param a:
        :return:
        """
        for i in a:
            self.append(i)

    def prepend(self, item):
        # case 1: when list is empty
        if self._first is None and self._last is None:
            node = Node(val=item)
            self._first = node
            self._last = node
        else:
            #case 2: when slist has at list one node.
            node = Node(val=item)
            node.next = self._first
            self._first = node

    def append(self, item):
        """
        appending list
        :param item:
        :return:
        """
        # case 1: when list os empty
        if self._first is None and self._last is None:
            node = Node(val=item)
            self._first = node
            self._last = node
        else:
            # case 2 when list of not empty
            node = Node(val=item)
            self._last.next = node
            self._last = node

    def find(self, item):
        """
        find item from list.
        :param item:
        :return:
        """
        tmp = self._first
        while tmp is not None:
            data = tmp.val
            if (data == item):
                return True
            tmp = tmp.next
        return False

    def delete(self, item):
        """
        delete item from a list
        :param item:
        :return:
        """
        ptr1 = self._first
        ptr2 = self._first
        # case 1: only single node and delete the targeted
        if len(self) == 1 and self.find(item):
            self._first = None
            self._last = None
        # node at first position
        elif ptr1.val == item and ptr1 == self._first:
            tmp = self._first
            tmp = tmp.next
            self._first = tmp
        # other than first position
        else:
            while ptr1 is not None:
                data = ptr1.val
                if data == item:
                    ptr2.next = ptr1.next
                    ptr1.next = ptr2.next
                ptr2 = ptr1
                ptr1 = ptr1.next
            self._last = ptr1

    def delete_last(self):
        ptr1 = self._first
        prvs = self._first
        while ptr1.next is not None:
            prvs = ptr1
            ptr1 = ptr1.next
        if prvs.next is not None:
            prvs.next = None
            self._last = prvs
        else:
            self._first = None
            self._last = None

    def __len__(self):
        """
        return length of singly linked list
        :return:
        """
        l_len = 0
        tmp = self._first
        while tmp is not None:
            l_len += 1
            tmp = tmp.next
        return l_len

    def __str__(self):
        """
        print singly linked list as str
        :return:
        """
        l_str = ""
        tmp = self._first
        while tmp != None:
            data = tmp.val
            l_str += str(data)
            l_str += "->"
            tmp = tmp.next
        l_str += "None"
        return l_str
