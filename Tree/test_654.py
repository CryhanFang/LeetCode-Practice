
#Java version


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return construct(nums,0,nums.length);

    }
    public TreeNode construct(int[] nums,int l,int r){
        if(l==r) return null;
        int max_i=max(nums,l,r);
        TreeNode root=new TreeNode(nums[max_i]);
        root.left=construct(nums,l,max_i);
        root.right=construct(nums,max_i+1,r);
        return root;
    }

    public int max(int[] nums,int l,int r){
        int max_i = l;
        for (int i=l;i<r;i++){
            if (nums[max_i]<nums[i])
                max_i=i;
        }
        return max_i;
    }
    
}


# Python version

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.construct(nums,0,len(nums))

    def construct(self,nums,l,r):
        if l==r:
            return None
        max_value=self.find_max_id(nums,l,r)
        root=TreeNode(nums[max_value])
        root.left=self.construct(nums,l,max_value)
        root.right=self.construct(nums,max_value+1,r)
        return root
    
    def find_max_id(self,nums,l,r):
        max_id=l
        for i in range(l+1,r):
            if nums[max_id]<nums[i]:
                max_id=i
        return max_id



