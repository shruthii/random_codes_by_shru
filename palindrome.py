
arr1= "malayalam"
l2=[""]*len(arr1)
i=-1
for x in arr1:
    l2[i]=x
    i-=1
arr2=''.join(l2)  
if arr1 == arr2:
    print('palindrome')
else:
    print('not')
    
    
    
    #####palindrome
    
    
    
arr1='malayalamo'
i,j=0,len(arr1)-1

while i!=j:
    if arr1[i] == arr1[j]:
        i+=1
        j-=1
        continue
    else:
        print("not a palindrome")
        break
else:
    print("Its a palindrome")
