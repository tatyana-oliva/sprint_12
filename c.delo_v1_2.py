def solution(node, idx):
    head = node

    index = 0
    node_prev = None
    while node is not None:
        if index == idx:
            if node_prev is None:
                head = node.next_item
            else:
                node_prev.next_item = node.next_item
            break

        node_prev = node
        node = node.next_item
        index = index + 1

    return head
