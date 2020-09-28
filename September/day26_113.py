"""
给定一个二叉树和一个目标和，找到所有从根节点到叶子节点路径总和等于给定目标和的路径。

说明: 叶子节点是指没有子节点的节点。

又学习到一个知识点,列表的复制!! 加不加[:] 的区别

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None

    def paths(self, root, total):
        ret = []
        path = []

        def dfs(root, total):
            if not root:
                return
            path.append(root.val)  # 根左右,加一个判断语句
            total -= root.val
            if not root.left and not root.right and total == 0:
                ret.append(path[:])  #
            dfs(root.left, total)
            dfs(root.right, total)
            path.pop()
        dfs(root, total)
        return ret
