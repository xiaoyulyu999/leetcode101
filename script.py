from collections import deque

from solution import Solution, TreeNode

solution = Solution()


# Main test
def create_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while i < len(arr):
        node = queue.popleft()

        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


if __name__ == '__main__':
    test_1 = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    test_2 = [1, 2, 3]
    test_3 = []
    tests = [(test_1, 22), (test_2, 5), (test_3, 0)]
    answers = [
        True, False, False
    ]
    for indx, test in enumerate(tests):
        rooter = create_tree(test[0])
        try:
            solution = Solution()
            r = solution.run(rooter, test[1])
            print(r)
            assert r == answers[indx]
            print("Test passed")
        except AssertionError:
            print("Test failed")
