from collections import deque

from solution import Solution, TreeNode

solution = Solution()


# Main test

def create_tree(arr):
    nodes = [TreeNode(var) for var in arr]
    queue = deque(nodes[::-1])

    root = queue.pop()
    for node in nodes:
        if node:
            node.left = queue.pop() if queue else None
            node.right = queue.pop() if queue else None
    return root


if __name__ == '__main__':
    test_1 = ([1, 2, 3], [1, 2, 3])
    test_2 = ([1, 2], [1, None, 2])
    test_3 = ([1, 2, 1], [1, 1, 2])
    tests = [test_1, test_2, test_3]
    answers = [
        True, False, False
    ]
    for indx, test in enumerate(tests):
        l, r = test
        l_root = create_tree(l)
        r_root = create_tree(r)
        try:
            solution = Solution()
            r = solution.run(l, r)
            print(r)
            assert r == answers[indx]
            print("Test passed")
        except AssertionError:
            print("Test failed")
