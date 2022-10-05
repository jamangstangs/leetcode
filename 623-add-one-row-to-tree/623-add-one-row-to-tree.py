# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # 자리 뺏길놈의 부모를 싹다 저장한다. -> 받은 depth -1 노드를 싹다 저장한다. 
        # 자리 뺏는 방법은 아래와 같다. 
        # 1. 자리 뺏긴놈을 새 노드로 설정,
        # 2. 자리 뺏긴놈의 부모의 자식 노드를 새 노드로 설정
        q = []
        target = depth-1
        q.append((root, 1))
        
        if depth == 1:
            nnode = TreeNode(val, None, None)
            nnode.left = root
            return nnode
        
        while q:
            node, cd = q.pop(0)
            if cd == target:
                    nnode = TreeNode(val, None, None)
                    ptr = node.left
                    node.left = nnode
                    nnode.left = ptr
                    nnode = TreeNode(val, None, None)
                    ptr = node.right
                    node.right =nnode
                    nnode.right = ptr
            else:
                if node.left != None:
                    q.append((node.left, cd+1))
                if node.right != None:
                    q.append((node.right, cd+1))
        return root