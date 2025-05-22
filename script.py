from solution import Solution, TreeNode

solution = Solution()


def create_tree(values):
    if not values:
        return None

    nodes = [TreeNode(x) for x in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
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
