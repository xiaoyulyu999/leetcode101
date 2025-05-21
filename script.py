from collections import deque

from solution import Solution, TreeNode

solution = Solution()
# Main test

def create_tree(values):
    if not values:
        return None

    tree_nodes_list = [TreeNode(var) if var is not None else None for var in values]
    queue = deque(tree_nodes_list)
    root = queue.pop()

    for node in tree_nodes_list:
        if node:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root

if __name__ == '__main__':

    try:
        solution = Solution()
        r = solution.run()
        assert r == 3
        print("Test passed")
    except AssertionError:
        print("Test failed")

