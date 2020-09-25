"""

根据一棵树的中序遍历与后序遍历构造二叉树。
注意:
你可以假设树中没有重复的元素。

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]

返回如下的二叉树：
【3,9,20,15,7] 前序遍历

这道题目的关键在于后序遍历的最后一位是根节点。类似的,前序遍历的第一位是根节点.
也就是说 前序/后序 + 中序 可以确定一个TreeNode.
流程大体是:
    1.找到根节点,也就是最后一位
    2.创建TreeNode类型
    3.递归
        终止条件: 后序遍历为空
        递归条件: 后序遍历不为空时:
                        递归创建新的节点, 这个时候应该是以root.left, root.right 为 主体.

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

class Solution:
    def buildTree(self, inorder, post):
        if not post:
            return
        root = TreeNode(post[-1])
        num = inorder.index(post[-1])
        root.left = self.buildTree(inorder[:num], post[:num])
        root.right = self.buildTree(inorder[num+1:], post[num:-1])
        return root



