def is_int(x):
    return isinstance(x, int)    

def f(ham: is_int, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return (str(ham) + ' and ' + eggs)

what = f('spam')
why = f(2)
print(what, type(what), why)

def merge_sort():
    '''
    Merge sort is a recursive algorithm that works by breaking down a list into smaller lists,
    then merging those smaller lists into larger, sorted lists.
    '''

def merge_sort_iterative(items):
    '''
    Merge sort implementation
    '''    
    

def merge_sort_recursive(items):
    '''
    Merge sort is a recursive algorithm that works by breaking down a list into smaller lists,
    then merging those smaller lists into larger, sorted lists.
    '''
    if len(items) > 1:
        mid = len(items) // 2
        left = items[:mid]
        right = items[mid:]

        merge_sort_recursive(left)
        merge_sort_recursive(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                items[k] = left[i]
                i += 1
            else:
                items[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            items[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            items[k] = right[j]
            j += 1
            k += 1

    


