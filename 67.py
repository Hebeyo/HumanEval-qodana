def fruit_distribution(s,n):
    # Your code here
    # split the string into a list of words
    s = s.split(' ')
    # create an empty list to store the number of apples and oranges
    lis = []
    # use a for loop to iterate through the list
    for i in s:
        # check if the element is a digit
        if i.isdigit():
            # if it is a digit, append it to the list
            lis.append(int(i))
    # return the number of mango fruits
    return n - sum(lis)

