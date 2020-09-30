"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

BFS
    1.使用deque的结构来模拟队列
    2. 有一个初始点
    3. 每次处理从队列中 pop出一个元素
    4. 对元素进行扩张 append
    5. 对扩张后满足条件的点再进行处理, 根据需要进入队列, 进入队列的点就是扩到下一层的点
    6. 循环处理deque中的元素,直到deque为空
    7. 输出结果.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lo(self, root):
        if not root:
            return []
        from collections import deque
        l = deque()
        l.append(root)
        res = []
        while l:
            cur_l = []
            for _ in range(len(l)):
                node = l.popleft()
                cur_l.append(node.val)
                if node.left:
                    l.append(node.left)
                if node.right:
                    l.append(node.right)
            res.append(cur_l)

        return res

    def level(self, root):
        from collections import deque
        queue = deque()
        queue.append(root)
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if not cur:
                    continue
                level.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            if level:
                res.append(level)
        return res
