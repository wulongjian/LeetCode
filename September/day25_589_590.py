"""
589. N叉树的前序遍历

真的是烦死我了,就是写不对~~~~
   def postorder(self, root: 'Node') -> List[int]:
        result = []
        def dfs(roots):
            if not roots:
                return
            childs = roots.children
            for child in childs:
                dfs(child)
            result.append(roots.val)
        dfs(root)
        return result
"""