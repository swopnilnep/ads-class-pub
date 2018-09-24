from stacks import Stack, StackError, TokenError

def rpn_calc(postfix_expr: str):
    '''Evaluate a postfix expression'''
    operand_stack = Stack()
    tokenList = postfix_expr.split()

    try:
        for token in tokenList:
            if token in "0123456789":
                operand_stack.push(int(token))
            else:
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(token,operand1,operand2)
                operand_stack.push(result)
        return operand_stack.pop()
    
    except TokenError:
        raise StackError

def do_math(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    else:
        raise TokenError("Unknown operation: {}".format(op))

def main():
    print(rpn_calc("1 2 3 +")) # Error
    print(rpn_calc("1 2 +")) # 3
    print(rpn_calc("1 4 * 4 +")) # 8

if __name__=="__main__":
    main()