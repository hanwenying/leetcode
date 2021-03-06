# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        node.val = node.next.val
        node.next = node.next.next
        """

        if node and node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            node = None

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    solution = Solution()
    solution.deleteNode(node2)
    print node1.val
