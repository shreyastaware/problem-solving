"""
The student wants to turn a minimum number of pages to get to page number `p` from either page number `1` or 
page number `n`. The number of pages they must turn from page number `1` is always `p/2`, but there is a 
twist when they start from the last page, page `n`:

If `n` is odd, then they turn `(n-p)/2` pages.
If `n` is even, then they turn `(n-p+1)/2` pages.
In Python 3, integer (floor) division makes it more simple:
"""

def pageCount(n, p):
    if not n%2:
        n += 1
    return min(p//2, (n-p)//2)
