'''Reverse Polish Notation'''

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

def rev_string_simple(my_str: str) -> str: # Complete
    '''Reverse characters in a string without using a stack'''
    return my_str[::-1]

def rev_string_stack(my_str: str) -> str: # Complete
    '''Reverse characters in a string using a stack'''
    string = Stack()
    for i in my_str:
        string.push(i)

    rev = ""
    for i in range(string.size()):
        rev += string.pop() 
    return rev
 
def par_checker(line: str) -> bool: # Complete
    '''Textbook implementation'''
    s = Stack()
    balanced = True
    i = 0
    while i < len(line) and balanced:
        symbol = line[i]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        i = i + 1
    if balanced and s.is_empty():
        return True
    else:
        return False

def par_checker_file(filename: str) -> None: # Complete
    '''Check expressions in the file'''
    with open(filename) as par_file:
        par = par_file.read().split("\n")
        output = ""
        for p in par:
            balanced = par_checker(p)
            if balanced: 
                output += ("{} is balanced".format(p) + "\n")
            else: 
                output += ("{} is NOT balanced".format(p) + "\n")
    print(output)

def base_converter(dec_num, base) -> str: # Complete
    '''Convert any decimal number to any base'''
    hex_digits = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    
    if base in [2,8,16]:
        
        remstack = Stack()

        while dec_num > 0:
            rem = dec_num % base
            remstack.push(rem)
            dec_num = dec_num // base

        new_string = ""
        while not remstack.is_empty():

            digit = remstack.pop()
            if digit >= 10: new_string = new_string + hex_digits[digit] # hex_digits[remstack.pop()]
            else: new_string += str(digit)

    else: 
        raise ValueError("Invalid base")

    return new_string

def rpn_calc(postfix_expr: str):
    '''Evaluate a postfix expression'''
    operand_stack = Stack()
    token_list = postfix_expr.split()

    try:
        for ind in range(len(token_list)):
            if token_list[ind] in "0123456789":
                # Seperates the operands in a Stack 
                operand_stack.push(int(token_list[ind]))
            elif token_list[ind] in "+-*/":
                # Does calculations with the operands 
                operand2 = operand_stack.pop()
                operand1 = operand_stack.pop()
                result = do_math(token_list[ind],operand1,operand2)
            
                # If the Stack still has elements 
                if ind == len(token_list) - 1 and not operand_stack.is_empty():
                    raise StackError("Stack is not empty")
                else:
                    operand_stack.push(result)
            else:
                raise TokenError("Unknown token: {}".format(token_list[ind]))
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
        raise TokenError("Unknown token: {}".format(op))

def main():

    '''String simple reverse'''
#     # print(rev_string_simple("123")) #321 
#     # print(rev_string_simple("123")) #321
#     # print(rev_string_simple("abc")) #cba 
#     # print(rev_string_simple("abc")) #cba
#     # print(par_checker_file('data/exercises/stacks/parentheses.txt'))

    '''String stack reverse'''
    # print(rev_string_stack("Hello"))

    '''Base conversion'''
#     # print(base_converter(1,2)) # 1
#     # print(base_converter(10,16)) # A
#     # print(base_converter(45,8)) # 55
#     # print(base_converter(10,10)) # Error 

    '''Reverse polish'''
    # print(rpn_calc("2 2 2 * +")) # Error
    # print(rpn_calc("a b +")) # Error
                    
if __name__=="__main__":
    main()
