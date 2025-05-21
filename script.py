from solution import Solution, TreeNode

solution = Solution()
# Main test


if __name__ == '__main__':

    try:
        solution = Solution()
        r = solution.run()
        assert r == 3
        print("Test passed")
    except AssertionError:
        print("Test failed")

