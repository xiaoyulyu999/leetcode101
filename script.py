from collections import deque

from solution import Solution, TreeNode

solution = Solution()


# Main test

def create_tree(arr):
    if not arr:
        return None

    nodes = [TreeNode(var) for var in arr]
    kids = deque(nodes[::-1])
    root = kids.pop()

    for node in nodes:
        if kids:
            node.left = kids.pop()
        if kids:
            node.right = kids.pop()

    return root


if __name__ == '__main__':
    test_1 = [3, 9, 20, None, None, 15, 7]
    test_2 = [1]
    test_3 = []
    tests = [test_1, test_2, test_3]
    answers = [
        [[15, 7], [9, 20], [3]],
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
