"""
# 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

这又是一个我没有遇到过的题型，这次也是遍历所有的节点，但是要遍历一次存储一次结果，之前是全部遍历完了返回结果。


假设从根节点到当前节点的和为val， 这个大问题可以转化为一个小问题，是否存在从当前节点的子节点到叶子的路径，
满足其路径和为sum-val。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def func(root: TreeNode, sum):
    """
    这也算是一个有用的函数了，可以改写成统计根节点到每个子节点的和。
    :param root:
    :param sum:
    :return:
    """
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == sum
    return func(root.left, sum -root.left) or func(root.right, sum-root.right)


def sunc(root):
    if not root:
        return 0
    if not root.left and not root.right:
        return root.val

