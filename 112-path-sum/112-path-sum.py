# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        ans = [False]
        
        def dfs(node, s):
            if node == None:
                return
            if node.left == None and node.right == None:
                if s+node.val == targetSum:
                    ans[0] = True
                return
            dfs(node.left, s + node.val)
            dfs(node.right, s + node.val)
            
        dfs(root, 0) 
        return ans[0]
            