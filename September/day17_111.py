"""
111 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。
"""


# 有用的代码块, 前序遍历求树的左右节点的深度。
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def get_depth(root: TreeNode):
    """
    逻辑是这样的，如果root为空，则返回0，如果不为空，而其左右子树全为空，那么返回1，
    最后的可能就是二者有一个不为空，或者全不为空，那么就依次求深度。
    :param root: TreeNode
    :return: ldepth, rdepth
    """

    if not root:
        return 0
    if not root.left and not root.right:
        return 1
    if root.left:
        ldepth = get_depth(root.left)+1
    if root.right:
        rdepth = get_depth(root.right)+1
    return ldepth, rdepth

