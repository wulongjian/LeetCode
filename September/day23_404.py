"""
# 404 左子叶之和
计算给定二叉树的所有左叶子之和
叶子说明是最后一层。

什么是叶子节点：
    一个节点即没有左子节点，也没有右子节点，该节点就是叶子节点

    如果该叶子节点是其父节点的左子节点， 就称为左子叶

前序、中序、后序？

终止条件
    不是左子节点


递归条件
    是左子节点： 递归到 为 左叶子节点为止。

"""