"""
demo singly linked list
"""


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LikedList:
    def __init__(self, head):
        self.head = head

    def length(self):
        cur = self.head
        counter = 0
        while cur != None:
            counter += 1
            cur = cur.next
        return counter

    def printList(self):
        cur = self.head
        str_lst = ""
        while cur != None:
            str_lst += str(cur.data)
            str_lst += "->"
            cur = cur.next
        str_lst += "Null"
        print(str_lst)

    def readValue(self, index):
        cur = self.head
        current_index = 0
        if cur == None:
            return -1
        if index >= self.length():
            print(index)
            print(self.length())
            return -1
        else:
            while cur != None and current_index != index:
                cur = cur.next
                current_index += 1
            return cur.data

    def searchItem(self, data):
        cur = self.head
        current_index = 0
        if cur == None:
            return -1
        else:
            while cur != None:
                if cur.data == data:
                    return current_index
                current_index += 1
                cur = cur.next
        return -1





a = Node("Jinesh")
b = Node("Patel")
c = Node("Hello")
d = Node("Hi")
a.next = b
b.next = c
c.next = d
#
# l = LikedList(a)
# print(l.searchItem("Hi"))
