"""
sort given liked list
"""


from slist2 import slist

s1 = slist()
s1.build_slist_from_list([4,3,2,1])


print(s1)


def sort_linked_list(head):
    c = head
    l = []
    while c:
        l.append(c.val)
        c = c.next
    l.sort()
    i = 0
    c = head
    while c:
        c.val = l[i]
        c = c.next
        i += 1
    return head

a = sort_linked_list(s1._first)

while a:
    print(a.val)
    a = a.next