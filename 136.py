def largest_smallest_integers(lst):
    smallest = None
    largest = None
    for i in lst:
        if i < 0:
            if smallest is None or i > smallest:
                smallest = i
        elif i > 0:
            if largest is None or i < largest:
                largest = i
    return smallest, largest
