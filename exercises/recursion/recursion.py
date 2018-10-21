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

def hourglass_rec(levels: int, space=0) -> None:
  str = (space * " ") + (2 * levels - 1) * "*"

  if levels == 1: 
    print(str)
    return

  print(str)  # print down 5, 4, 3, 2, 1
  hourglass_rec(levels - 1, space + 1)  # recursion point
  print(str)

def diamond_rec(levels: int, space=0) -> None:
      
  str = (levels * " ") + (2 * space + 1) * "*"
  
  if levels == 1: 
    print(str)
    return

  print(str)
  diamond_rec(levels - 1, space + 1)  # recursion point
  print(str)

def main():
    '''Main function'''
    hourglass_ite(10)
    hourglass_rec(10)
    diamond_ite(10)
    diamond_rec(10)


if __name__ == '__main__':
    main()
