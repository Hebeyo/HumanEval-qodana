def total_match(lst1, lst2):
    # Your code here
    # create two variables to store the total number of chars in the two lists
    l1 = 0
    l2 = 0
    # use a for loop to iterate through the first list
    for st in lst1:
        # add the length of each string to l1
        l1 += len(st)
    # use a for loop to iterate through the second list
    for st in lst2:
        # add the length of each string to l2
        l2 += len(st)
    # if l1 is less than or equal to l2, return the first list
    if l1 <= l2:
        return lst1
    # otherwise return the second list
    else:
        return lst2
