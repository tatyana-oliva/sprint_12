# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(node):
    nodes = []

    index = 0
    while node is not None:
        nodes.append(node)
        index = index + 1
        node = node.next_item

    # print(index)

    index = index - 1
    while index >= 0:
        print(nodes[index].value)
        index = index - 1


if LOCAL:
    def test():
        node3 = Node("node3", None)
        node2 = Node("node2", node3)
        node1 = Node("node1", node2)
        node0 = Node("node0", node1)
        solution(node0)
        # Output is:
        # node0
        # node1
        # node2
        # node3

    if __name__ == '__main__':
        test()
