def is_sorted(lst):
    # Your code here
    # use a for loop to iterate through the list
    for i in range(1, len(lst)):
        # if the element at index i is less than the element at index i-1, return False
        if lst[i] < lst[i-1]:
            return False
    # use a for loop to iterate through the list
    for i in range(1, len(lst)-1):
        # if the element at index i is equal to the element at index i-1 and i+1, return False
        if lst[i] == lst[i-1] and lst[i] == lst[i+1]:
            return False
    # otherwise return True
    return True
