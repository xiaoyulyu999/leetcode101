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
    test_1 = [1, 2, 2, 3, 4, 4, 3]
    test_2 = [1, 2, 2, None, 3, None, 3]
    test_3 = [1, 2, 2, None, 3, 3, None]
    tests = [test_1, test_2, test_3]
    answers = [
        True, False, True
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
