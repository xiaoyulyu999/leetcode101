from solution import Solution

solution = Solution()
# Main test


if __name__ == '__main__':
    test_1 = [2, 7, 11, 15]
    test_2 = [3, 2, 4]
    test_3 = [3, 3]
    tests = [(test_1, 9), (test_2, 6), (test_3, 6)]
    answers = [
        [0, 1],
        [1, 2],
        [0, 1]
    ]
    for indx, test in enumerate(tests):
        try:
            ls, target = test
            solution = Solution()
            r = solution.run(ls, target)
            print(r)
            assert r == answers[indx]
            print("Test passed")
        except AssertionError:
            print("Test failed")
