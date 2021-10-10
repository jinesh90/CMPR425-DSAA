"""
example of good and bad fibonacci
"""

def bad_fibo(n):
    if n <= 1:
        return n
    else:
        return bad_fibo(n-1) + bad_fibo(n-2)


def good_fibo(n):
    if n <=1:
        return n,0
    else:
        a,b = good_fibo(n-1)
        return a+b, a


print(good_fibo(25))
print(bad_fibo(25))
