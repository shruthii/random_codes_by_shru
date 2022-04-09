num1,num2= 2341,0

l=len(str(num1))
l1=l-1
for i in range(l):
    last_digit= int(num1%10)
    new_num=int(last_digit * (10**(l1)))
    num2+=new_num
    l1-=1
    num1=int(num1/10)
    
print(num2)  



#reversing an integer
