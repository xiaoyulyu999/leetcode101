from solution import Solution, TreeNode

solution = Solution()
# Main test


if __name__ == '__main__':
    test_1 = [2,7,11,15]
    test_2 = [3,2,4]
    test_3 = [3,3]
    tests = [test_1, test_2, test_3]
    answers = [
        9,
        6,
        6
    ]
    for indx, test in enumerate(tests):
        try:
            solution = Solution()
            r = solution.run(rooter)
            print(r)
            assert r == answers[indx]
            print("Test passed")
        except AssertionError:
            print("Test failed")