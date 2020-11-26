"""
872. 叶子相似的树
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。

首先, 找出树的叶值序列; 然后比较他们是否相等.

要找出树的叶值序列,可以使用dfs, 如果节点是叶子, dfs会写入结点的值,然后递归的探索每个子节点.
这可以保证从左到右访问每片叶子.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def ls(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)
        return list(dfs(root1)) == list(dfs(root2))


"""
判断叶子节点的方法
if not node.right and not node.left:
    为叶子节点
"""

