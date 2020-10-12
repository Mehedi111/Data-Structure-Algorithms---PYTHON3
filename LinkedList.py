'''
Head is a pointer
Data | Next = NODE
'''


class Node:
    data = 0
    next = None

    @staticmethod
    def create_node(item, next_node):
        node = Node()
        node.data = item
        node.next = next_node

        return node

    @staticmethod
    def remove_node(head, node):
        if head == node:  # check that remove node is equal with head position or 1st item, then we just next the head
            head = node.next
            return head

        # If node is not head means this node is after head
        current_node = head  # keep the head in current node

        while current_node is not None:  # Increase current node position by next to reach the removable node reference
            if current_node.next == node:
                # if current node.next (next node ref) is the removable node reference then break loop
                break

            #  Assign each time next node reference to current node if not get the removable node
            current_node = current_node.next

        #  Now check that whether node is Not found ?
        #  if yes than return head
        if current_node is None:
            return head

        #  We got the node that is before the removable node, so just change the next item from
        #  removable node to current node
        current_node.next = node.next
        return head

    @staticmethod
    def insert_node_at_first(head, item):
        #  For add in 1st at Linked List, just create node [Item, head] , new item with head reference
        #  Then change head position.
        new_node = Node().create_node(item, head)
        return new_node

    @staticmethod
    def insert_node_at_last(head, item):
        inserted_node = Node().create_node(item, None)
        if head is None:
            return inserted_node

        #  For add in last at Linked List, We need to iterate list to get node which has null reference
        #  then just create node [Item, None]
        #  after that add this node to the last item
        while head.next is not None:
            head = head.next
            #  Complexity O(n)

        if head.next is None:
            head.next = inserted_node

        return head


def get_last_node(head):
    c_head = head
    while c_head.next is not None:
        c_head = c_head.next
        #  Complexity O(n)

    return c_head


if __name__ == '__main__':
    new_node4 = Node().create_node(8, None)

    new_node3 = Node().create_node(18, new_node4)

    new_node2 = Node().create_node(12, new_node3)

    new_node1 = Node().create_node(10, new_node2)

    head = new_node1
    print(head.data)

    #  Remove node
    # after removed node 3, node 3  is the reference in head.

    print(f"Before removed 2nd node is : {head.next.data}")
    head = Node().remove_node(head, new_node2)
    print(f"after removed 2nd node is : {head.next.data}")

    #  Insert node at 1st
    head = Node().insert_node_at_first(head, 15)
    print(f"1st item after insert at 1st : {head.data}")
    print(f"2nd item after insert at 1st :{head.next.data}")

    #  Insert node at last
    print(f"Last item before insert at last : {get_last_node(head).data}")
    head = Node().insert_node_at_last(head, 100)
    print(f"Last item after insert at last :{get_last_node(head).data}")
