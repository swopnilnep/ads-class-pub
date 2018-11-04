'''
Touchscreen Keyboard
'''
#!/usr/bin/env python3

import sys
import re

def get_string(filename: str) -> str:
    '''Takes in the filename of the output and returns a string as the entire file, throws and exception if not run'''
    try:
        with open(filename) as inputFileHandle:
            return inputFileHandle.read()

    except IOError:
        sys.stderr.write( "[myScript] - Error: Could not open %s\n" % (filename) )
        sys.exit(-1)

def get_dict_from_str(keystrokes: str) -> dict:
    '''Takes the raw file and returns a dictionary with key as the original word and values as the suggestions in the db'''
    
    words = re.split("[\s\n]+", keystrokes) # Uses regular expression (faster with longer texts to split newline and spaces)
    test_count = int(words[0])
    words = words[1:len(words) - 1] # Removes the first (assigned to test_count) and last (empty srting) values of the words list 
        
    all_words = {}

    for i in range(test_count):    
        length = int(words[1])
        name = words[0]
        suggestions = words[2: 2 + length]
        words = words[2 + length ::]

        all_words[name] = suggestions

    return all_words

def spell_check(filename: str) -> str:
    '''
    1. Takes in a word, checks in with the value suggestions 
    2. Ranks the closest word and prints the output
    '''

    raw_data = get_string(filename) # Takes in the raw data from the file
    words = get_dict_from_str(raw_data) # Takes the words in the string and converts into a dictionary {'original':[list of suggested]}

    # Dictionary that assigns each character with a cartesian coordinate 
    character_map = \
    {'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4), 'y': (0, 5), 'u': (0, 6), 'i': (0, 7), 'o': (0, 8), 'p': (0, 9), 
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4), 'h': (1, 5), 'j': (1, 6), 'k': (1, 7), 'l': (1, 8), 
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3), 'b': (2, 4), 'n': (2, 5), 'm': (2, 6)}

    def get_loc(c):
        return character_map[c]

    def distance(a, b):
        dist = 0
        for i in range(len(a)):
            dist += int( abs( a[i][0] - b[i][0]) + abs(a[i][1] - b[i][1]) )
        return dist

    # Main string output 
    output = ""

    for key, values in words.items():

        # Output string within loop
        out = ""

        # Locations of the keys
        key_loc = [] 
        for k in key:
           key_loc.append(get_loc(k))

        # Lists of the locations of the values 
        values_loc = []
        value_names = []
        for value in values:
            value_names.append(value)
            # Locations of the values 
            value_sub = []
            for v in value:
                value_sub.append(get_loc(v))
            values_loc.append(value_sub)

        dist_old = 0
        name_old = ""

        for i in range(len(values_loc)):
            
            dist = distance(key_loc, values_loc[i])
            name = value_names[i]

            if dist > dist_old:
                out = out + ("{} {}\n").format(value_names[i],dist)

            elif dist < dist_old:
                out = ("{} {}\n").format(value_names[i],dist) + out
            
            elif dist == dist_old:
                
                if name > name_old: out = out + ("{} {}\n").format(value_names[i],dist)
                elif name < name_old : out = ("{} {}\n").format(value_names[i],dist) + out

            dist_old = dist 
            name_old = name 

        output += out

    print(output)
    print(output.split("\n"))

def main():
    '''Entry point'''
    spell_check('data/projects/keyboard/sample.in') # Uses the spellcheck algorithm on the words, returns an output

if __name__ == '__main__':
    main()
