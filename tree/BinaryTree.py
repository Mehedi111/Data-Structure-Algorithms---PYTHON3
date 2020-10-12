'''
WE GONNA IMPLEMENT IT
               2
             /   \
           7      9
         /  \      \
        1    6      8

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def create_tree():
        node_two = Node(2)
        node_seven = Node(7)
        node_nine = Node(9)
        node_six = Node(6)
        node_eight = Node(8)
        node_one = Node(1)

        #  add child to root
        node_two.add_left_child(node_seven)
        node_two.add_right_child(node_nine)

        node_seven.add_left_child(node_one)
        node_seven.add_right_child(node_six)

        node_nine.add_right_child(node_eight)

        return node_two

    @staticmethod
    def print_all_degree(node_two):
        print(f"root {node_two.data}")
        print(f"Left of root : {node_two.data} is {node_two.left.data}")
        print(f"Right of root : {node_two.data} is {node_two.right.data}")

        print(f"Left of : {node_two.left.data} is {node_two.left.left.data}")
        print(f"Right of : {node_two.left.data} is {node_two.left.right.data}")

        print(f"Right of : {node_two.right.data} is {node_two.right.right.data}")

    def add_left_child(self, child):
        self.left = child

    def add_right_child(self, child):
        self.right = child

    def pre_order(self, node):
        print(node.data)

        if node.left is not None:
            self.pre_order(node.left)

        if node.right is not None:
            self.pre_order(node.right)

    def post_order(self, node):

        if node.left is not None:
            self.post_order(node.left)

        if node.right is not None:
            self.post_order(node.right)

        print(node.data)

    def in_order(self, node):

        if node.left is not None:
            self.in_order(node.left)
        print(node.data)

        if node.right is not None:
            self.in_order(node.right)
