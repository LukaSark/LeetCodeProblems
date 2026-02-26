# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        Strings = []
        def dfs(root, string):
            
            if root is None:
                return
            
            string += str(root.val)
            
            if root.left is None and root.right is None:
                Strings.append(string)
                return
            
            dfs(root.left, string)
            dfs(root.right, string)
        
        dfs(root, "")
        
        output = 0
        for s in Strings:
            output += int(s, 2)

        return output
