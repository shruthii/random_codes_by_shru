str1=list("fluster")
str2=list("restful")

if len(str1) != len(str2):
    print("its not an anagram!")
str1.sort()
str2.sort()

for x in range(len(str1)):
    if str1[x]== str2[x]:
        continue
    else:
        print("its not an anagram!")
        break
else:
    print("Its an anagram")
    
    
    
    #find whether 2 strings are anagram or not
