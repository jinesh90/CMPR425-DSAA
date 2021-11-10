"""
merge two lists like l1 = [1,2,4], l2 = [1,3,4]
return [1,1,2,3,4,4]
"""
from slist2 import slist

s1 = slist()
s2 = slist()

s1.build_slist_from_list([1, 2, 4, 5, 6])
s2.build_slist_from_list([1, 3, 4])

s3 = slist()

head1 = s1._first
head2 = s2._first

while head1 != None or head2 != None:
    if head1 != None:
        val1 = head1.val
    else:
        val1 = 1000
    if head2 != None:
        val2 = head2.val
    else:
        val2 = 1000

    if val1 >= val2:
        s3.append(val2)
        head2 = head2.next
    else:
        s3.append(val1)
        head1 = head1.next


print(s3)





