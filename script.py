from collections import deque

from solution import Solution, TreeNode

solution = Solution()


def create_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        current = queue.popleft()

        # Left child
        if i < len(arr) and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        # Right child
        if i < len(arr) and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

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
            r = solution.run(l_root, r_root)
            print(r)
            assert r == answers[indx]
            print("Test passed")
        except AssertionError:
            print("Test failed")
