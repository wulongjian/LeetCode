"""
二叉搜索树的最近公共祖先

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

二叉搜索树.

两次遍历:  -----会超时
    1. 从根节点开始遍历
    2. 如果当前节点是P, 成功找到了节点
    3. 如果 当前节点大于P, P在当前节点的左子树
    4. 如果 当前节点小于P,P在当前节点的右子树
    5. 在寻找节点的过程中, 顺便记录经过的节点
    6. P和q的最近公共祖先就是从根节点到他们路径上的分叉点.
    7. 找出最大的编号i, 使其满足 path_p[i] = path_q[i], 对应的节点就是公共祖先
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def la(self, root, p, q):
        def getPath(root, target):
            path = []
            node = root
            while node != target:
                path.append(node)
                if target.val < node.val:
                    node = root.left
                else:
                    node = root.right
            path.append(node)
            return path
        path_p = getPath(root, p)
        path_q = getPath(root, q)
        ancestor = None
        for u, v in zip(path_p, path_q):
            if u == v:
                ancestor = u
            else:
                continue
        return ancestor


"""
一次遍历:
    1. 从根节点开始遍历 `----前序遍历?
    2. 如果当前节点的值大于pq的值, 说明pq应该在当前节点的左子树
    3. 如果当前节点的值小于pq的值,说明pq应该在当前节点的右子树
    4. 如果不满足上述两条要求, 说明当前节点就是分岔点, 
    5. pq要么在当前节点的不同子树中,要么其中一个就是当前节点.
    6. 如果将这两个节点放在一起遍历,就省去了存储路径需要的空间
"""
class TreeNode2:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution2:
    def la(self, root, p, q):
        ans = root
        while 1:
            if p.val < ans.val and q.val < ans.val:
                ans = ans.left
            elif p.val > ans.val and q.val > ans.val:
                ans = ans.right
            else:
                break
        return ans