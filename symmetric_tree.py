#TC: O(n) 
#SC:O(h)
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 


        result = [ ]
        self.dfs(root, 0, result)
        for i in result: #after getting all the nodes level wise, now check whether palindrome or not
            if not self.isPalindrome (i): 
                return False 

        return True       
        
    def dfs(self, root, level, result):
        
        if len(result) < level+1: #if there's no level, append an empty list
            result.append([ ]) 
        if root: 
            result[level].append(root.val) #if there is a node, append it
        else: 
            result[level].append(None) #else append the None
        if root: 
            #call the dfs recursively on left and right with leveling up and result as parameter
            self.dfs(root.left,  level+1, result)   
            self.dfs(root.right, level+1, result)  

    def isPalindrome(self,li): #function to find whether a list is palindrome or not
        left = 0
        right = len(li)-1

        while left<=right: #two pointer approach to find the similarity between first half and second half
            if li[left]!=li[right]:                                                                                             
                return False
    
            left+=1 #inrement the left pointer
            right-=1 #decrement the right pointer

        return True