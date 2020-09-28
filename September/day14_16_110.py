"""
110 平衡二叉树，两种解题方式，自顶向下的递归，自下向上的递归

自上向下： 前向遍历， 根左右，
终止条件:
    root 为空
递归条件:
    计算左右子树的深度


自下向上： 后序遍历， 左根右。
    添加了剪枝操作,只要有一个子树不满足,树整体就不满足
    左跟右,,然后加上一个判断条件.
    返回值:
        1. 当节点root左右子树的深度差小于等于1,返回当前子树的深度, 即 max(left, right)+1
        2. 当节点root左右子树的深度差大于2, 返回-1, 代表此子树不是平衡树
    终止条件:
        1. 当root为空
        2. 当深度为-1

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

    # 这就是一个剪枝操作
    if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) + 1


