# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
       	self.left = None
      	self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    solution = Solution()
    if solution.isSameTree(node1, node2):
        print 'hello world'
