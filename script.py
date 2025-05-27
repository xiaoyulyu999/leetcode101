from solution import Solution

solution = Solution()
# Main test


if __name__ == '__main__':
    test_1 = "abcabcbb"
    test_2 = "bbbbb"
    test_3 = "pwwkew"
    tests = [(test_1, 3), (test_2, 1), (test_3, 3)]
    answers = [
        [0, 1],
        [1, 2],
        [0, 1]
    ]
    for indx, test in enumerate(tests):
        try:
            ls, target = test
            solution = Solution()
            r = solution.run(ls)
            print(r)
            assert r == target
            print("Test passed")
        except AssertionError:
            print("Test failed")
