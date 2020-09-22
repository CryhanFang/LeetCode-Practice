# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        '''
        Preorder traversal
        '''
        # if original==None:
        #     return None
        # if original.val==target.val:
        #     return cloned

        # res=self.getTargetCopy(original.left,cloned.left,target)
        # if res != None:
        #     return res
        
        # res=self.getTargetCopy(original.right,cloned.right,target)

        # if res!=None:
        #     return res
        # return None


        #########BFS
        stack = []
        clonedstack = []
        node=original
        clonet = cloned

        while node != None or len(stack)!=0:
            if node !=None:
                if node.val == target.val:
                    return clonet
                stack.append(node)
                node=node.left
                clonedstack.append(clonet)
                clonet=clonet.left
            else:
                node=stack.pop(0)
                node=node.right
                clonet=clonedstack.pop(0)
                clonet=clonet.right

        return None

