'''
 [x | A | r_B ] -> <- [r_A | B | r_c] -><- [r_b | C | r_d] -><- [r_c | D |x]
 note: r_B means reference of B
        x means Empty
        So Node A has previous Empty reference and Next has B node reference,
        and Node B has previous A node reference and Next has C node reference
        \n
        at last node D has previous node C reference and next has no reference so it is Empty
'''


class Node:
    data = 0
    next = None
    prev = None

    @staticmethod
    def create_node(prev, item, next_node):
        node = Node()
        node.data = item
        node.next = next_node
        node.prev = prev

        return node

    @staticmethod
    def append(node1, node2):
        node1.next = node2
        return node1

    @staticmethod
    def add_at_first(item, n1):
        new = Node().create_node(None, item, n1)
        n1.prev = new
        return new

    @staticmethod
    def add_at_last(item, head):
        cur = head
        while cur.next is not None:
            cur = cur.next

        new = Node().create_node(cur, item, None)
        cur.next = new
        return head

    @staticmethod
    def delete_node(head, rm_node):
        cr = head

        while cr.next is not None:
            if cr.next == rm_node:
                #  got previous node of removable node
                break
            cr = cr.next

        cr.next = rm_node.next
        rm_node.next.prev = cr
        return head




def travers_node(text, node):
    print(text)
    while node is not None:
        print(node.data)
        node = node.next


if __name__ == '__main__':
    #  Create 4 node with next reference empty
    n1 = Node().create_node(None, 10, None)
    n2 = Node().create_node(n1, 12, None)
    n3 = Node().create_node(n2, 14, None)
    n4 = Node().create_node(n3, 16, None)

    #  add next node reference to each node
    n1 = Node().append(n1, n2)
    n2 = Node().append(n2, n3)
    n3 = Node().append(n3, n4)

    head = n1
    travers_node("All items after 4 node creation", head)

    new = Node().add_at_first(5, head)
    head = new

    travers_node("All items after add one item at first", head)

    new = Node().add_at_last(50, head)
    head = new
    travers_node("All items after add one item at last", head)

    new = Node().delete_node(head, head.next)
    head = new
    travers_node("All items after remove 2nd node", head)

