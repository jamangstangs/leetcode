import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if root == None:
            return []
        def helper(node, route, cursum, target):
            croute = route.copy()
            croute.append(node.val)
            cursum = cursum + node.val
   
            if node.right == None and node.left == None:
                if cursum == target:
                    ans.append(croute)
                return 
            if node.left != None:
                helper(node.left, croute, cursum, target)
            
            if node.right != None:
                helper(node.right, croute, cursum, target)
                
        helper(root, [], 0, targetSum)
        return ans
            