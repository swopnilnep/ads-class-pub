'''
Touchscreen Keyboard
'''
#!/usr/bin/env python3

import sys

def dist_letters(l1 : str, l2 : str) -> int:
    character_map = \
    {'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9), 
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8), 
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)}

    d1 = character_map[l1]
    d2 = character_map[l2]

    return int(abs(d1[0] - d2[0]) + abs(d1[1] - d2[1]))

def dist_words(w1: str, w2: str) -> int:


def spell_check(filename: str) -> None:
    '''Rank words by their proximity to the target'''
    raise NotImplementedError

def main():
    '''Entry point'''
    # spell_check('data/projects/keyboard/sample.in')

    # print(dist_letters('w', 'q')) # 1 
    # print(dist_letters('s', 'e')) # 2 
    # print(dist_letters('v', 'q')) # 5 
        

if __name__ == '__main__':
    main()