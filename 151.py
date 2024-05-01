def double_the_difference(lst):
    sum = 0
    for i in lst:
        if i > 0 and i%2!=0 and "." not in str(i):
            sum += i**2
    return sum
