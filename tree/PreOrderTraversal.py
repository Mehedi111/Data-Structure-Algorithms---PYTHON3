from tree.BinaryTree import Node

'''
    PRE_ORDER_TRAVERSE:
    root -> Left -> Right
    
    WE GONNA IMPLEMENT IT
               2
             /   \
           7      9
         /  \      \
        1    6      8

'''

if __name__ == "__main__":
    tree = Node.create_tree()
    Node.print_all_degree(tree)

    print("Pre_Order result ")
    print(tree.pre_order(tree))

    print("Post_Order result ")
    print(tree.post_order(tree))

    print("in_Order result")
    print(tree.in_order(tree))


