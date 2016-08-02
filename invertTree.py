# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self._invert_tree(root)
        return root

    def _invert_tree(self, root):
        if not root:
            return
        root.left, root.right = root.right, root.left
        self._invert_tree(root.left)
        self._invert_tree(root.right)

if __name__ == '__main__':
    root = TreeNode(1)
    left = TreeNode(2)
    right = TreeNode(3)
    root.left = left
    root.right = right
    solution = Solution()
    root = solution.invertTree(root)
    print root.val, root.left.val, root.right.val
