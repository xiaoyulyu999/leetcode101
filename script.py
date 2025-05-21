from solution import Solution, TreeNode

solution = Solution()

def build_tree(values):
    if not values:
        return None

    nodes = [TreeNode(x) if x is not None else None for x in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root

# Main test
if __name__ == '__main__':
    tree_list = [1,4,3,7,6,8,5,None,None,None,None,9,None,10]

    root = build_tree(tree_list)

    solution = Solution()
    r = solution.run(root)
    print(r) #---3