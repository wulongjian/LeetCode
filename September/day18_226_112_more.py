"""
翻转一棵二叉树。
这个问题曾经做过一遍，现在又不会做了。真的是陷进去了。。。

以后做题一定要问自己这么三个问题
1. 这是什么遍历：前序、中序、还是后序
2. 他的递归条件是什么
3. 他的终止条件是什么
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


def invertTree(root):
    # 终止条件，递归到叶子节点，或者root为空
    if not root:
        return

    # 递归条件，如果不为空，或不为子节点，那么交换该节点的左右节点
    root.left, root.right = root.right, root.left

    # 这是一个前序遍历
    invertTree(root.left)
    invertTree(root.right)
    return root
