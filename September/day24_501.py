"""
给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

    结点左子树中所含结点的值小于等于当前结点的值
    结点右子树中所含结点的值大于等于当前结点的值
    左子树和右子树都是二叉搜索树

# 自己的代码
执行结果：
通过
显示详情
执行用时：72 ms, 在所有 Python3 提交中击败了64.71% 的用户
内存消耗：17.4 MB, 在所有 Python3 提交中击败了15.26% 的用户

## 最简单的大佬写法，看着太舒服了。。。。！！！！
def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        # 第一想法是哈希表记录
        Hash = {}
        def dfs(root, Hash):
            if not root:
                return
            Hash[root.val] = Hash.get(root.val, 0) + 1
            dfs(root.left, Hash)
            dfs(root.right, Hash)
        dfs(root, Hash)
        mode = max(Hash.values())
        return [key for key in Hash.keys() if Hash[key] == mode]

# 如何不占用额外内存呢
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
#
# class Solution:
#     def findMode(self, root: TreeNode):
#         self.r = []
#         def help(root):
#             if not root:
#                 return
#             self.r.append(root.val)
#             help(root.left)
#             help(root.right)
#         from collections import Counter
#         help(root)
#         c = Counter(self.r)
#         r2 = list(c.values())
#         r2.sort(reverse=True)
#         w = sum([r2[0]==x for x in r2])
#         r3 = c.most_common(w)
#         result = []
#         for i in r3:
#             result.append(int(i[0]))
#         return result


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None
        self.left = None


class Solution:
    def __init__(self):
        self.pre = None
        self.ret = []
        self.ret_count, self.max_count, self.cur_count = 0, 0, 0

    def findMode(self, root: TreeNode):
        self.inOrder(root)
        self.pre = None
        self.ret = [0] * self.ret_count
        self.ret_count, self.cur_count = 0, 0
        self.inOrder(root)
        return self.ret

    def inOrder(self, root: TreeNode) -> None:
        if not root:
            return
        self.inOrder(root.left)
        if self.pre and self.pre.val == root.val:
            self.cur_count += 1
        else:
            self.cur_count = 1
        if self.cur_count > self.max_count:
            self.max_count = self.cur_count
            self.ret_count = 1
        elif self.cur_count == self.max_count:
            if len(self.ret):
                self.ret[self.ret_count] = root.val
            self.ret_count += 1
        self.pre = root
        self.inOrder(root.right)

## 最简单易懂的一种方法
def findMode(self, root: TreeNode):
    if not root:
        return []
    # 第一想法是哈希表记录
    Hash = {}

    def dfs(root, Hash):
        if not root:
            return
        Hash[root.val] = Hash.get(root.val, 0) + 1
        dfs(root.left, Hash)
        dfs(root.right, Hash)

    dfs(root, Hash)
    mode = max(Hash.values())
    return [key for key in Hash.keys() if Hash[key] == mode]