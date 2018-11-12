"""Tree building exercise"""
#!/usr/bin/env python3


def BinaryTree(r):
    return [r, [], []]


def insert_child_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_child_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_child_left(root):
    return root[1]


def get_child_right(root):
    return root[2]

def clockwise(root):
    """Clockwise tree traversal"""
    print(get_root_val(root), end=" ")
    if get_child_right(root):
        clockwise(get_child_right(root))
    if get_child_left(root):
        clockwise(get_child_left(root))

def build_tree_lst() -> list:
    """Build a tree and return it"""
    t = BinaryTree('a')
    # Level 1
    insert_child_left(t, 'b')
    insert_child_right(t, 'c')
    # Level 2
    insert_child_right(get_child_left(t), 'd')
    insert_child_left(get_child_right(t), 'e')
    insert_child_right(get_child_right(t), 'f')
 
    return t

def main():
    t = build_tree_lst()

    # Test Cases
    assert get_root_val(t) == 'a'
    assert get_root_val(get_child_left(t)) == 'b'
    assert get_root_val(get_child_right(t)) == 'c'
    assert get_root_val(get_child_right(get_child_left(t))) == 'd'
    assert get_root_val(get_child_left(get_child_right(t))) == 'e'
    assert get_root_val(get_child_right(get_child_right(t))) == 'f'

if __name__== "__main__":
    main()