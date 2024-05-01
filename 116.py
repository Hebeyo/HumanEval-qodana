def sort_array(arr):
    # Your code goes here
    return sorted(sorted(arr), key=lambda x: bin(x)[2:].count('1'))
