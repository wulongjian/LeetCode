"""
110 平衡二叉树，两种解题方式，自顶向下的递归，自下向上的递归

自上向下： 前向遍历， 根左右，

自下向上： 后序遍历， 左根右。

"""


class TreeNode:
    def __init__(self, root):
        self.val = root
        self.left = None
        self.right = None


def help(root):
    """
    有用的代码块
    :param root: TreeNode
    :return: depth, 树的深度
    """
    if not root: return 0
    return max(help(root.right), help(root.left)) + 1


def height(root):
    """
    :param root: TreeNode
    :return:
    """
    if not root:
        return 0
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    # 当depth第n层为left-right>1时，那么它的根节点那一层就表现为 left=-1 or right=-1
    if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) + 1


