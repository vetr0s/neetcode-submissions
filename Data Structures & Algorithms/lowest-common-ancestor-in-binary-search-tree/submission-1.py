# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        p_val = p.val
        q_val = q.val
        while cur:
            cur_val = cur.val
            if cur_val > p_val and cur_val > q_val:
                cur = cur.left
            elif cur_val < p_val and cur_val < q_val:
                cur = cur.right
            else:
                return cur