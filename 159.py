def eat(number, need, remaining):
    # Write your code here
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]

