# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levelVals = {}
        def dfs(node, depth):
            if node is None:
                return
            if depth not in levelVals.keys():
                levelVals[depth] = 0
            levelVals[depth] += node.val
            
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        
        dfs(root, 1)
        maxNum = float('-inf')
        res = 0
        for k, v in levelVals.items():
            if maxNum < v:
                maxNum = v
                res = k

        return res 