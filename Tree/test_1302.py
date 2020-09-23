# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''

利用一个全局变量去约束depth的信息以及total 总量的信息，然后在深度优先搜索的时候，进行不断的更新，通过去和max dep的判断去进行一个更新，并且把
depth=max depth的内容结合在一起后去记录信息
'''
class Solution(object):
    def __init__(self):
        self.maxdep = -1
        self.total = 0
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,depth):
            if not node:
                return 
            if depth>self.maxdep:
                self.maxdep, self.total=depth,node.val
            elif depth==self.maxdep:
                self.total+=node.val
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
        
        dfs(root,0)
        return self.total



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''

通过把id和root信息结合在一起，来标记每一个root和id的信息，因为是广度优先搜索，所以会到最后一层的时候才会更新max dep，区别于深度优先搜索，很有可能很快搜到max 所以需要全局变量
广度优先搜索，会在最后一层叠加
'''
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        q = collections.deque([(root, 0)])
        maxdep, total = -1, 0
        while len(q) > 0:
            node, dep = q.pop()
            if dep > maxdep:
                maxdep, total = dep, node.val
            elif dep == maxdep:
                total += node.val
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))
        return total



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        q = [(root, 0)]#collections.deque([(root, 0)])
        maxdep, total = -1, 0
        while len(q) > 0:
            node, dep = q.pop(0)
            if dep > maxdep:
                maxdep, total = dep, node.val
            elif dep == maxdep:
                total += node.val
            if node.left:
                q.append((node.left, dep + 1))
            if node.right:
                q.append((node.right, dep + 1))
        return total