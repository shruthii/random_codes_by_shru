arr=[0,1,2,1,2,0,0]
i,j=0,0
k= len(arr)-1

while j<=k:
    if arr[j]<1:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j+=1
        #print('less than 1',arr)
        
    
    elif arr[j]==1:
        j+=1
        #print('equal to 1',arr)
        
        
    elif arr[j]>1:
        arr[k],arr[j]=arr[j],arr[k]
        k-=1
        #print('greater than 1',arr)
        
print(arr)
    
    
    
    
    #dutch flag problem
