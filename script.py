from collections import deque

from solution import Solution, TreeNode

solution = Solution()
# Main test

def create_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])



if __name__ == '__main__':

    try:
        solution = Solution()
        r = solution.run()
        assert r == 3
        print("Test passed")
    except AssertionError:
        print("Test failed")

