from collections import deque

from solution import Solution, TreeNode

solution = Solution()
# Main test

def create_tree(values):
    if not values:
        return None

    tree_nodes_list = [TreeNode(var) if var is not None else None for var in values]
    queue = deque(tree_nodes_list[::-1])
    root = queue.pop()

    for node in tree_nodes_list:
        if node:
            node.left = queue.pop() if queue else None
            node.right = queue.pop() if queue else None
    return root

if __name__ == '__main__':
    test_1 = [0, -1]
    test_2 = [1, 2, 3]
    test_3 = [1, 3, 2, 5, 3, None, 9]
    tests = [test_1, test_2, test_3]
    answers = [
        [0, -1],
        [1, 3],
        [1, 3, 9]
    ]
    for indx, test in enumerate(tests):
        rooter = create_tree(test)
        try:
            solution = Solution()
            r = solution.run(rooter)
            print(r)
            assert r == answers[indx]
            print("Test passed")
        except AssertionError:
            print("Test failed")

