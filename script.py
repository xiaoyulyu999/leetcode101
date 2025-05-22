from collections import deque

from solution import Solution, TreeNode

solution = Solution()


# Main test
def create_tree(arr):
    if not arr:
        return None
    nodes = [TreeNode(var) for var in arr]
    leafs = deque(nodes[::-1])
    root = leafs.pop()

    for node in nodes:
        if node:
            node.left = leafs.pop() if leafs else None
            node.right = leafs.pop() if leafs else None
    return root


if __name__ == '__main__':
    test_1 = [3, 9, 20, None, None, 15, 7]
    test_2 = [1]
    test_3 = []
    tests = [test_1, test_2, test_3]
    answers = [
        [[3], [9, 20], [15, 7]],
        [[1]],
        []
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
