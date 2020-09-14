import json


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 108
"""
有序数组== BST中序遍历、升序排列
难点
1.数组如何变成treenode：  逐元素递归：TreeNode(num)
2.如何平衡左右字数 ：    取中间元素作为根节点
"""


class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def helper(left, right):
            if left > right: return None
            mid = (left+right+1)//2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid-1)
            root.right = helper(mid+1, right)
            return root
        return helper(0, len(nums)-1)
