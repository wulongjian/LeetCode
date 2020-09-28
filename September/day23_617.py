"""
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，
否则不为 NULL 的节点将直接作为新二叉树的节点。

我觉得这个使用前序遍历，以root为递归,而不是root.left or root.right. ！！！！！如果将结果保存在Tree1中，那么这个应该是
        后序遍历 !!! 其实也不是，这个前序后序就是看你怎么写代码了。。。

终止条件：
    如果两个root全为空， 结束。

递归条件：
    如果两个root全部不为空，那么这两个root相加
    如果其中一个root为空，
        root1为空:  r1.val = r2.val
        root2为空: r2.val = None, r1保持不变



"""
# 虽然分析的头头是道，但是我的代码却是一塌糊涂
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        报错信息如下。
        AttributeError: 'NoneType' object has no attribute 'val'.
            t1.val = t2.val
        :param t1:
        :param t2:
        :return:
        """
        if not t1 and not t2:
            return
        if t1 and t2:
            t1.val = t1.val + t2.val
        elif not t1:
            t1.val = t2.val
        elif not t2:
            return t1
        self.mergeTrees(t1.left, t2.left)
        self.mergeTrees(t1.right, t2.right)
        return t1


"""
  说到底还是递归条件想错了
    递归条件：
    如果两个root全部不为空，那么这两个root相加
    如果其中一个root为空，
        root1为空:  r1.val = r2.val !! 直接返回root2
        root2为空: r2.val = None, r1保持不变 !! 直接返回root1
    
"""


def mt(t1, t2):
    if not t1:
        return t2
    if not t2:
        return t1
    t1.val = t1.val + t2.val  # 这个写在这里，就是前序遍历
    t1.left = mt(t1.left, t2.left)
    t1.right = mt(t1.right, t2.right)

    # t1.val = t1.val + t2.val  这样就是后序遍历

    return t1
