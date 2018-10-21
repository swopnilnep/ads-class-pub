'''Recursion exercise code template'''

#!/usr/bin/env python3


def gcd(a: int, b: int) -> int:
    if a == 0 or b == 0: return a + b
    else: return gcd(b,a%b)

def hourglass_ite(levels: int) -> None: 
    adder = -1
    initial_value = levels
    while levels <= initial_value:
        print(" " * (initial_value - levels) + "*" * (2 * levels - 1))
        levels += adder
        if levels == 1: adder *= -1

def diamond_ite(levels: int) -> None:
    adder = - 1
    initial_value = levels
    while levels <= initial_value:
        
        ast = 2 * (initial_value - levels) + 1
        spaces = levels 
        
        print(" " * spaces + "*" * ast)

        levels += adder
        if levels == 1: adder *= -1

def hourglass_rec(levels: int, initial=levels) -> None:
    initial = levels
    if levels == initial + 1: return None
    print(levels)
    hourglass_rec(levels - 1, initial)
    
    

def diamond_rec(levels: int) -> None:
    raise NotImplementedError

def main():
    '''Main function'''
    # hourglass_ite(5)
    hourglass_rec(5)
    # diamond_ite(5)
    # diamond_rec(5)


if __name__ == '__main__':
    main()
