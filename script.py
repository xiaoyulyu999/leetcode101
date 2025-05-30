from solution import Solution

solution = Solution()
# Main test


if __name__ == '__main__':
    test_1 = 3749
    test_2 = 58
    test_3 = 1994
    tests = [(test_1, "MMMDCCXLIX"), (test_2, "LVIII"), (test_3, "MCMXCIV")]
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
