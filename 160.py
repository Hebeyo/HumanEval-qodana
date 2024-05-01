def do_algebra(operator, operand):
    # Your code here
    # create an expression variable to store the expression
    expression = ''
    # use a for loop to iterate through the operator list
    for i in range(len(operator)):
        # add the element at index i of the operand list to expression
        expression += str(operand[i])
        # add the element at index i of the operator list to expression
        expression += operator[i]
    # add the last element of the operand list to expression
    expression += str(operand[-1])
    # return the evaluation of expression
    return eval(expression)
    