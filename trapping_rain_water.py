class Solution:
    def trap(self, height: List[int]) -> int:
        max_left=[0]*len(height)
        max_right=[0]*len(height)
        
        #print('max_left =',max_left)
        #print('max_right =',max_right)
        
        for i in range(1,len(height)):
            max_left[i]= max(max_left[i-1],height[i-1])
            
        #print('max_left=',max_left) 
        
        #a=[1,2,3,4]
        
        for i in range(-2,-len(height)-1,-1):
            max_right[i]=max(max_right[i+1],height[i+1])
            
        #print('max_right=',max_right)
        w_count=0
        for x in range(len(height)):
            w = min(max_left[x],max_right[x])-height[x]
            if w >0:
                w_count+=w
        #print('w_count=',w_count)  
        return w_count
        
        
        
        #Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

