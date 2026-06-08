# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = []
        queue.append(root)
        if not root:
            return res

        while queue:
            levelSize = len(queue)
            currentLevel = []

            for _ in range(levelSize):
                node = queue.pop(0)
                currentLevel.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(currentLevel)
        return res