from solution import Solution

solution = Solution()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [1,2,1,0,0,0]
    queries = [[0,3],[2,4]]
    r = solution.isZeroArray(nums, queries)
    print(r)