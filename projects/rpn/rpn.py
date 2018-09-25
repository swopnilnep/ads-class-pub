# CS160A
# Project 3 (rmp_calculator)
# Swopnil N. Shrestha (shresw01)


'''
Reverse Polish Notation
'''
#!/usr/bin/env python3


class Stack:
    '''Stack implementation'''
    def __init__(self):
        self._items = []

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

    def push(self, new_item):
        self._items.append(new_item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

class StackError(Exception):
    '''Stack errors'''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class TokenError(Exception):
    '''Token errors'''
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

def postfix_eval(postfix_expr: str) -> int:
    '''Evaluate the postfix expression'''

    postfix_expr = postfix_expr.strip().strip("=")
    operand_stack = Stack()
    token_list = postfix_expr.split()
    if len(token_list) == 0: raise StackError("Stack is empty")
    
    try:
        for ind in range(len(token_list)):

            if token_list[ind].isdigit():

                # Seperates the digits in a Stack 
                operand_stack.push(int(token_list[ind]))

            elif token_list[ind] in ["**","//","%","="]:
                
                # Does calculations with the operands 
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                
                try:
                    result = do_math(token_list[ind],operand1,operand2)
                except ZeroDivisionError:
                    return "ERROR: integer division or modulo by zero"

                # If the Stack still has elements 
                if ind == len(token_list) - 1 and not operand_stack.is_empty():
                    raise StackError("ERROR: Stack is not empty")
                else:
                    operand_stack.push(result)

            elif token_list[ind] in "+-*/":
                
                # Does calculations with the operands 
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                
                try:
                    result = do_math(token_list[ind],operand1,operand2)
                except ZeroDivisionError:
                    return("ERROR: division by zero")

                # If the Stack still has elements 
                if ind == len(token_list) - 1 and not operand_stack.is_empty():
                    raise StackError("Stack is not empty")
                else:
                    operand_stack.push(result)

            else:
                raise TokenError("Unknown token: {}".format(token_list[ind]))
        return(operand_stack.pop())
        
    except IndexError:
        return ("ERROR: pop from empty list")

def do_math(op: str, op1: int, op2: int) -> int:

    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "%":
        return op1 % op2    
    elif op == "**":
        return op1 ** op2
    elif op == "//":
        return op1 // op2    
    else:
        raise TokenError("Unknown operation: {}".format(op))

def rpn_calc(filename: str) -> int:
    
    try:
        with open(filename) as inputFileHandle:
            test_string = inputFileHandle.read()

            test_list = test_string.strip("\n").split("\n")
            sum = 0

            for postfix_expr in test_list:
                
                result = postfix_eval(postfix_expr)
                
                if isinstance(result, int) or isinstance(result, float):
                    sum += result
                print(postfix_expr + " " + str(result))

            return sum

    except IOError:
        return "ERROR: File not found"


def main():

    checksum = rpn_calc('data/projects/rpn/rpn_input_1.txt')

    if isinstance(checksum, str):
        print(checksum) 
    else:
        print('Checksum is %.2f' % checksum)
        


if __name__ == '__main__':
    main()

