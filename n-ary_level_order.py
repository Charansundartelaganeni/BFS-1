#TC: O(n)
#SC: O(h) - height of the tree is 'h'
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]: 


        q = deque([root]) #q will be our queue and it contains the root
        result = []  #open a resultant list

        while q:  #traverse through the q

            size = len(q) #size of q is important to traverse through the entire level
            temp = [] 
            
            for i in range(size): #traverse through the level
                
                node = q.popleft()  #node will be first ele in q
                if node:   #if there's a node, append that into temp level
                    temp.append(node.val)
                    
                    for i in node.children: #now traverse through the children of the node

                        q.append(i)   
                    
            if len(temp) >= 1: #if it has atleast only one child,then append temp to result
                result.append(temp) 

        return result