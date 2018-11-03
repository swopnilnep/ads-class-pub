from stacks import Stack, StackError, TokenError

def rpn_calc(postfix_expr: str):
    '''Evaluate a postfix expression'''
    operand_stack = Stack()
    token_list = postfix_expr.split()
    
    print(postfix_expr)
    print(token_list)

    try:
        for ind in range(len(token_list)):
            if token_list[ind] in "0123456789":
                # Seperates the operands in a Stack 
                operand_stack.push(int(token_list[ind]))
            else:
                # Does calculations with the operands 
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(token_list[ind],operand1,operand2)
            
                # If the Stack still has elements 
                if ind == len(token_list) - 1 and not operand_stack.is_empty():
                    raise StackError("Unknown expression {}".format(postfix_expr))
                else:
                    operand_stack.push(result)
                    return(operand_stack.pop())
    except IndexError:
        raise StackError("Stack is empty")


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

# def main():
#     # (rpn_calc("1 +")) # Returns Index Error
#     # (rpn_calc("1 4 3 +")) # Returns Stack Error
#     # (rpn_calc("2 3 4 + +")) # 9

#     # assert rpn_calc('1 2 3 + -') == -4

# if __name__=="__main__":
#     main()