"""
adding two lists like 895 + 78
"""
from slist2 import slist

s1 = slist()
s2 = slist()
s3 = slist()


def add_two_num(n1, n2):
    n1_list = []
    n2_list = []
    n3_list = []
    while n1 > 0:
        n1_list.append(n1 % 10)
        n1 //= 10
    while n2 > 0:
        n2_list.append(n2 % 10)
        n2 //= 10

    # now we get lists
    s1.build_slist_from_list(n1_list)
    s2.build_slist_from_list(n2_list)

    head1 = s1._first
    head2 = s2._first
    c = 0
    while head1 != None or head2 != None:
        if head1 != None:
            val1 = head1.val
        else:
            val1 = 0
        if head2 != None:
            val2 = head2.val
        else:
            val2 = 0
        s = val1 + val2 + c
        c = s // 10
        last_digit = s % 10

        n3_list.append(last_digit)

        if head1 != None:
            head1 = head1.next
        if head2 != None:
            head2 = head2.next
    if c > 0:
        n3_list.append(c)

    s3.build_slist_from_list(n3_list)
    s3.reverse()
    print(s3)


add_two_num(123, 123)




