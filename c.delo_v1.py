# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = True

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


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


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)

    print('before:')
    node = node0
    while node is not None:
        print(node.value)
        node = node.next_item

    new_head = solution(node0, 1)

    print('after:')
    node = node0
    while node is not None:
        print(node.value)
        node = node.next_item

    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
