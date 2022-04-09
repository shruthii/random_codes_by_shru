class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        sub_arr,sub_s=[],[]
        x=0
        while x<=len(s)-1:
            for i in range(x,len(s)):
                #print('i=',i)
                if s[i] not in sub_s:
                    sub_s.append(s[i])
                else:
                    #print('sub_s=',sub_s)
                    sub_arr.append(sub_s)
                    sub_s=[]

                    #print('sub_arr=',sub_arr)
                    break
                    #continue
            x+=1 
        sub_arr_len=[len(x) for x in sub_arr]   
        return max(sub_arr_len) if (len(sub_arr_len) >0) else 0
        #print(sub_arr)
        
        #Given a string s, find the length of the longest substring without repeating characters.
