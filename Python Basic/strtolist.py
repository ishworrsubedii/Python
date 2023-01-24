def Convert(string):
    li = list(string.split(" "))
    return li
  
# Driver code    
str1 = "Geeks for Geeks"
for i in str1:
    print(i)
    duplicate=set(str1)
    # print(duplicate)
    message=str1.count(i)
    print(i,message)
print(Convert(duplicate))