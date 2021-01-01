RED = 0
BLACK = 1
DOUBLE_BLACK = 2

class TreeNode:
    def __init__(self, key, value, color):
        self.key = key
        self.value = value
        self.color = color
        self.left_child = None
        self.right_child = None
        self.parent = None
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _readable_str(self):
        color = 'RED' if self.color == 0 else 'BLACK'
        return f'{self.key}, {color}'

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if is_nil(self.right_child) and is_nil(self.left_child):
            line = self._readable_str()
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if is_nil(self.right_child):
            lines, n, p, x = self.left_child._display_aux()
            s = self._readable_str()
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if is_nil(self.left_child):
            lines, n, p, x = self.right_child._display_aux()
            s = self._readable_str()
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_child._display_aux()
        right, m, q, y = self.right_child._display_aux()
        s = self._readable_str()
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

NIL = TreeNode(0, 0, BLACK)
DOUBLE_BLACK_NODE = TreeNode(0, 0, DOUBLE_BLACK)

def is_red_node(node):
    return node.color == RED

def is_black_node(node):
    return node.color == BLACK

def is_double_black_node(node):
    return node.color == DOUBLE_BLACK

def create_tree_node(key, value, color):
    node = TreeNode(key, value, color)
    node.parent = node.left_child = node.right_child = NIL
    return node

def add_child(parent, child, left):
    if left:
        parent.left_child = child
    else:
        parent.right_child = child
    child.parent = parent

def remove_child(parent, child):
    new_child = NIL
    if not is_nil(child.left_child):
        new_child = child.left_child
    if not is_nil(child.right_child):
        new_child = child.right_child

    if parent.left_child == child:
        parent.left_child = new_child
    else:
        parent.right_child = new_child
    child.parent = NIL
    return new_child

def replace_child(parent, child, new_child):
    if parent.left_child == child:
        parent.left_child = new_child
    else:
        parent.right_child = new_child
    new_child.parent = parent
    return new_child

def is_nil(node):
    return node == NIL

def is_leaf(node):
    return node.left_child == NIL and node.right_child == NIL

def find_parent(start, key):
    result = start.parent
    current = start
    left = True
    while not is_nil(current):
        result = current
        if key < current.key:
            current = current.left_child
            left = True
        else:
            current = current.right_child
            left = False
    
    return result, left

def find_node(start, key):
    current = start
    while not is_nil(current):
        if current.key == key:
            return current

        if key < current.key:
            current = current.left_child
        else:
            current = current.right_child
    
    return None

def find_min_successor(start):
    result = start
    current = start.right_child
    while not is_nil(current):
        result = current
        current = current.left_child
    return result

def get_parent(node):
    return node.parent

def get_sibling(node):
    parent = get_parent(node)
    if parent.left_child == node:
        return parent.right_child
    else:
        return parent.left_child

def set_color_to(node, color):
    node.color = color

def right_rotate(node):
    new_parent = node.left_child
    new_parent.right_child = node
    new_parent.parent = node.parent
    node.parent = new_parent
    node.left_child = NIL
    return new_parent

def left_rotate(node):
    new_parent = node.right_child
    new_parent.left_child = node
    new_parent.parent = node.parent
    node.parent = new_parent
    node.right_child = NIL
    return new_parent

def is_root(node):
    return node.parent == NIL

def switch_node(node1, node2):
    node1.key, node2.key = node2.key, node1.key
    node1.value, node2.value = node2.value, node1.value

def pull_black(node):
    node.color += 1
    if node.left_child == DOUBLE_BLACK_NODE:
        node.left_child = NIL
    else:
        node.left_child.color -= 1
    
    if node.right_child == DOUBLE_BLACK_NODE:
        node.right_child = NIL
    else:
        node.right_child.color -= 1

def flip_right(node):
    original_parent = node.parent
    original_node = node
    new_parent = node.left_child

    node.left_child = node.left_child.right_child
    node.left_child.parent = node

    new_parent.right_child = node
    new_parent.parent = node.parent
    node.parent = new_parent
    set_color_to(new_parent, BLACK)
    set_color_to(new_parent.right_child, RED)
    replace_child(original_parent, original_node, new_parent)
    return new_parent

def flip_left(node):
    original_parent = node.parent
    original_node = node
    new_parent = node.right_child

    node.right_child = node.right_child.left_child
    node.right_child.parent = node

    new_parent.left_child = node
    new_parent.parent = node.parent
    node.parent = new_parent
    set_color_to(new_parent, BLACK)
    set_color_to(new_parent.left_child, RED)
    replace_child(original_parent, original_node, new_parent)
    return new_parent

def push_black(node):
    node.color -= 1
    node.left_child.color += 1
    node.right_child.color += 1

def fix_right_doubleblack_left_black(node):
    pull_black(node)
    if is_red_node(node.left_child.right_child) and is_black_node(node.left_child.left_child):
        node.left_child = left_rotate(node.left_child)
    if is_red_node(node.left_child.left_child):
        node = flip_right(node)
        push_black(node)
    return node

def fix_right_double_black(node):
    if is_red_node(node.left_child):
        node = flip_right(node)
        node.right_child = fix_right_doubleblack_left_black(node.right_child)
        return node
    else:
        return fix_right_doubleblack_left_black(node)

def fix_left_doubleblack_right_black(node):
    pull_black(node)
    if is_red_node(node.right_child.left_child) and is_black_node(node.right_child.right_child):
        node.right_child = right_rotate(node.right_child)
    if is_red_node(node.right_child.right_child):
        node = flip_left(node)
        push_black(node)
    return node

def fix_left_double_black(node):
    if is_red_node(node.right_child):
        node = flip_left(node)
        node.left_child = fix_left_doubleblack_right_black(node.left_child)
        return node
    else:
        return fix_left_doubleblack_right_black(node)

class RedBlackTree:
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        return self.root is None
    
    def search(self, key):
        return find_node(self.root, key)

    def insert(self, key, value):
        if self.is_empty():
            root = create_tree_node(key, value, BLACK)
            self.root = root
            return root
        else:
            new_node = create_tree_node(key, value, RED)
            parent, left = find_parent(self.root, new_node.key)
            add_child(parent, new_node, left)
            if is_red_node(parent):
                grand_parent = get_parent(parent)
                uncle = get_sibling(parent)
                if is_red_node(uncle):
                    if not is_root(grand_parent):
                        set_color_to(grand_parent, RED)
                    set_color_to(uncle, BLACK)
                    set_color_to(parent, BLACK)
                else:
                    # uncle's color is black
                    if parent == grand_parent.right_child:
                        if parent.left_child == new_node:
                            parent = right_rotate(parent)
                            grand_parent.right_child = parent
                            new_node = parent.right_child
                        
                        if parent.right_child == new_node:
                            parent = left_rotate(grand_parent)
                            get_parent(parent).right_child = parent
                            set_color_to(parent, BLACK)
                            set_color_to(parent.left_child, RED)
                            if is_root(parent):
                                self.root = parent
                    else:
                        if parent.right_child == new_node:
                            parent = left_rotate(parent)
                            grand_parent.left_child = parent
                            new_node = parent.left_child

                        if parent.left_child == new_node:
                            parent = right_rotate(grand_parent)
                            get_parent(parent).left_child = parent
                            set_color_to(parent, BLACK)
                            set_color_to(parent.right_child, RED)
                            if is_root(parent):
                                self.root = parent

    def remove(self, key):
        node = find_node(self.root, key)
        if node is None:
            return

        if not is_nil(node.left_child) and not is_nil(node.right_child):
            #internal node
            new_node = find_min_successor(node)
            switch_node(new_node, node)
            node = new_node

        if is_red_node(node):
            # Red
            remove_child(node.parent, node)
        else:
            # Black
            if is_leaf(node):
                new_child = replace_child(node.parent, node, DOUBLE_BLACK_NODE)
                node = new_child
                while is_double_black_node(node):
                    if node.parent.right_child == node:
                        node = fix_right_double_black(node.parent)
                    else:
                        node = fix_left_double_black(node.parent)
                    if is_root(node):
                        if node == DOUBLE_BLACK_NODE:
                            self.root = NIL
                        set_color_to(node, BLACK)

            else:
                red_leaf_child = remove_child(node.parent, node)
                set_color_to(red_leaf_child, BLACK)

    def print(self):
        self.root.display()

if __name__ == '__main__':
    red_black_tree = RedBlackTree()
    red_black_tree.insert(13, 9)
    red_black_tree.insert(8, 8)
    red_black_tree.insert(17, 7)
    red_black_tree.insert(1, 9)
    red_black_tree.insert(11, 8)
    red_black_tree.insert(15, 7)
    red_black_tree.insert(25, 9)
    red_black_tree.insert(6, 8)
    red_black_tree.insert(22, 7)
    red_black_tree.insert(27, 7)
    #red_black_tree.insert(39, 7)
    #red_black_tree.insert(12, 7)
    #red_black_tree.insert(18, 7)
    red_black_tree.remove(15)
    red_black_tree.print()
    #print(red_black_tree.search(22).key)