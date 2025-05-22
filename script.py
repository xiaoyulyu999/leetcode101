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
            if leafs:
                node.left = leafs.pop()
            if leafs:
                node.right = leafs.pop()
    return root


if __name__ == '__main__':
    test_1 = [1, 2, 2, 3, 4, 4, 3]
    test_2 = [1, 2, 2, None, 3, None, 3]
    # test_3 = [1, 3, 2, 5, 3, None, 9]
    tests = [test_1, test_2]
    answers = [
        True, False
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
