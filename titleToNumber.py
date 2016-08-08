class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        :reduce(lambda x, y: x + y, list, initialization)
        """
        l = map(lambda x: ord(x) - ord('A') + 1, list(s))
        num = reduce(lambda x, y: 26 * x + y, l)
        return num


if __name__ == '__main__':
    solution = Solution()
    print solution.titleToNumber('Z')
