"""
669. 修剪二叉搜索树
给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L)
你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。

"""


def trimBST(root, l , r):
    if not root:
        return None
    if root.val < l:
        return trimBST(root.right, l, r)
    if root.val > r:
        return trimBST(root.left, l, r)
    root.left = trimBST(root.left, l, root.val)
    root.right = trimBST(root.right, root.val, r)


"""
令trim(node)作为该节点上的子树的理想答案.我们可以递归的构建该答案
当node.val > R, 修剪后的二叉树必定出现在节点的左边
当node.val < L, 修剪后的二叉树出现在节点的右边
"""


class Solution:
    def trimbst(self,root, l, r):
        def trim(node):
            if not node:
                return None
            elif node.val < l:
                return trim(node.right)
            elif node.val > r:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
            return node
        return trim(root)

