from solution import Solution

solution = Solution()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,0,1]
    queries = [[0,2]]
    r = solution.isZeroArray(nums, queries)
    print(r)