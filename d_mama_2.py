def solution(node, elem):
    index = 0
    while node is not None:
        if node.value == elem:
            return index

        node = node.next_item
        index = index + 1
    return -1
