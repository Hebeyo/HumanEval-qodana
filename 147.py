def get_max_triples(n):
    # Your code here
    # create a list to store the values of a
    a = []
    # use a for loop to iterate through the numbers from 1 to n
    for i in range(1, n+1):
        # append i*i-i+1 to the list
        a.append(i*i-i+1)
    # create a variable to store the number of triples
    count = 0
    # use a for loop to iterate through the list
    for i in range(len(a)):
        # use a for loop to iterate through the list
        for j in range(i+1, len(a)):
            # use a for loop to iterate through the list
            for k in range(j+1, len(a)):
                # if the sum of the elements is divisible by 3
                if (a[i]+a[j]+a[k])%3 == 0:
                    # increase the count by 1
                    count += 1
    # return the count
    return count
