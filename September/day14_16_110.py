"""
110 平衡二叉树，两种解题方式，自顶向下的递归，自下向上的递归

"""


def help(root):
    """
    有用的代码块
    :param root: TreeNode
    :return: n能够返回左右子树中最大的那个
    """
    if not root: return True
    return max(help(root.right), help(root.left)) + 1
