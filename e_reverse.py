def solution(node):
    prev_node = None
    while node is not None:
        prev = node.prev
        next = node.next

        node.prev = next
        node.next = prev

        prev_node = node
        node = next

    return prev_node
