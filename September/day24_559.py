"""
559. N叉树的最大深度

给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

这里一个就是～～～二叉树我们可以使用root.left , root.right来递归每个root的子节点，
N叉树如何遍历呢， ！！ 写一个循环就好了， 列表表达式。

有用的代码块
[self.maxDepth(root) for root in root.children]
"""


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        elif not root.children:
            return 1
        else:
            depth = [self.maxDepth(root) for root in root.children]
        return max(depth)
