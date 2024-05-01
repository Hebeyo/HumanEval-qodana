def move_one_ball(arr):
    # Your code here
    # create a copy of the list
    my_arr = arr.copy()
    # use a for loop to iterate through the list
    for i in range(len(arr)):
        # if the list is sorted, return True
        if sorted(my_arr) == my_arr:
            return True
        # otherwise, shift the elements of the list by one position to the right
        my_arr = [my_arr[-1]] + my_arr[0:-1]
    # if the list is sorted, return True
    if sorted(my_arr) == my_arr:
        return True
    # otherwise, return False
    return False
