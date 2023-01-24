# Python code to convert string to list character-wise


def Convert(string):
    list1=[]
    list1[:0]=string
    return list1
# Driver code
str1="This is a commmon interview question"
print(Convert(str1))

duplicate=set(str1)
print(duplicate)
x=str1.count(duplicate)
duplicate

# print("duplicate:",duplicate)
# for i in str1:
#     
#     print(i,x)
