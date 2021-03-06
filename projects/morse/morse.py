"""Morse code encoding and decoding"""
#!/usr/bin/env python3
# encoding: UTF-8


class BinaryTree:
    """Binary Tree implementation as nodes and references"""

    def __init__(self, key):
        self._key = key
        self._child_left = None
        self._child_right = None

    def get_root_val(self):
        """Get root key value"""
        return self._key

    def set_root_val(self, new_key):
        """Set root key value"""
        self._key = new_key

    def get_child_left(self):
        """Get left child"""
        return self._child_left

    def set_child_left(self, new_child_left):
        """Set left child"""
        self._child_left = new_child_left

    def get_child_right(self):
        """Get right child"""
        return self._child_right

    def set_child_right(self, new_child_right):
        """Set right child"""
        self._child_right = new_child_right

    def is_leaf(self):
        """Check if a node is leaf"""
        return (not self._child_left) and (not self._child_right)

    def insert_left(self, new_node):
        """Insert left subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_left != None:
            new_subtree.set_child_left(self._child_left)
        self._child_left = new_subtree

    def insert_right(self, new_node):
        """Insert right subtree"""
        new_subtree = BinaryTree(new_node)
        if self._child_right != None:
            new_subtree.set_child_right(self._child_right)
        self._child_right = new_subtree

    def preorder(self):
        """Pre-order tree traversal"""
        print(self._key, end=" ")
        if self._child_left:
            self._child_left.preorder()
        if self._child_right:
            self._child_right.preorder()

    def inorder(self):
        """In-order tree traversal"""
        if self._child_left:
            self._child_left.inorder()
        print(self._key, end=" ")
        if self._child_right:
            self._child_right.inorder()

    def postorder(self):
        """Post-order tree traversal"""
        if self._child_left:
            self._child_left.postorder()
        if self._child_right:
            self._child_right.postorder()
        print(self._key, end=" ")

class Coder:
    """Morse Code Encoder/Decoder"""

    def __init__(self, file_in: str):
        """Constructor"""
        self.morse_tree = BinaryTree('')

        with open(file_in) as morse_file:
            for line in morse_file:
                letter, code = line.split()
                self.follow_and_insert(code, letter)


    def follow_and_insert(self, code_str: str, letter: str):
        """Follow the tree and insert a letter"""
        current = self.morse_tree
        
        for symbol in code_str:        
            if symbol == '.':
                if current.get_child_left() == None:
                    current.insert_left('')
                current = current.get_child_left()
            if symbol == '-':
                if current.get_child_right() == None:
                    current.insert_right('')
                current = current.get_child_right()
        """set the current node value to _letter_"""
        current.set_root_val(letter)

    def follow_and_retrieve(self, code_str: str):
        """Follow the tree and retrieve a letter"""
        current = self.morse_tree
        for symbol in code_str:
            """if _dot_, go to to the left child, else go to the right child"""
            if symbol == '.':
                if current != None:
                    current = current.get_child_left()
            if symbol == '-':
                if current != None:
                    current = current.get_child_right()

        """return the current node value"""
        if current != None:

            return current.get_root_val()


    def find_path(self, tree: object, letter: str, path: str):
        """Find a key"""
        if tree == None: return False        
        elif tree.get_root_val() == letter: return path
        else: return self.find_path(tree.get_child_left(), letter, path+'.') or self.find_path(tree.get_child_right(), letter, path+'-')

    def encode(self, msg: str):
        """Encode a message"""
        code = ''
        path = ''
        for word in msg.split():
            for letter in word:
                coded = str(self.find_path(self.morse_tree, letter, path)) + ' '
                code = code + coded
                if code == "False ": raise ValueError("Could not encode {}: {} is not in the tree".format(msg,letter))
        return code

    def decode(self, code: str):
        """Decode a message"""
        msg = ''
        for letter in code.split():
            if self.follow_and_retrieve(letter) != None:

                msg += self.follow_and_retrieve(letter)
            else:
                raise ValueError("Could not decode {}: {} is not in the tree".format(code, letter))
        return msg


def main():
    morse_coder = Coder("data/projects/morse/morse.txt")

    '''Follow and insert tests '''
    # print(morse_coder.tree.get_child_left().get_root_val()) # e
    # print(morse_coder.tree.get_child_right().get_child_left().get_root_val()) # n
    # print(morse_coder.tree.get_child_right().get_root_val()) # t
    # print(morse_coder.tree.get_child_right().get_child_right().get_child_left().get_child_left().get_root_val()) # z

    '''Follow and retrieve tests'''
    # print(morse_coder.follow_and_retrieve('.')) # e
    # print(morse_coder.follow_and_retrieve('-.')) # n
    # print(morse_coder.follow_and_retrieve('-')) # t
    # print(morse_coder.follow_and_retrieve('--..')) # z

    '''Find path tests '''
    # morse_coder.find_path(morse_coder.tree, "f", "")

    print("Encoding 'sos'")
    print("Expected: ... --- ...")

    print("Encoded : {}".format(morse_coder.encode("sos")))
    print("---")
    print("Encoding 'data structures'")
    print("Expected: -.. .- - .- ... - .-. ..- -.-. - ..- .-. . ... ")
    print("Encoded : {}".format(morse_coder.encode("data structures")))
    print("---")
    print("Encoding '$$'")
    print("Expected: Error message")
    try:
        print("Encoded : {}".format(morse_coder.encode("$$")))
    except ValueError as ve:
        print("ERROR: {}".format(ve))
    print("---")
    print("Decoding '.... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----'")
    print("Expected: hello,cs160")
    test_str = ".... . .-.. .-.. --- --..-- -.-. ... .---- -.... -----"
    print("Decoded : {}".format(morse_coder.decode(test_str)))

if __name__ == "__main__":
    main()
