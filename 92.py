def any_int(x, y, z):
    # Your code here
    # use the if statement to check if all numbers are integers
    if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
        # use the if statement to check if one of the numbers is equal to the sum of the other two
        if x + y == z or x + z == y or y + z == x:
            # if yes, return True
            return True
        # if no, return False
        else:
            return False
    # if no, return False
    else:
        return False
    
