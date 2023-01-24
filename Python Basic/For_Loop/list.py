#  duplicate remover program

# 1
list=[1,2,2,2,2,2,3,4,5,6,7,7]
k=0

for i in list:
    k+=1


    for j in range(k,len(list)):
        if i==list[k]:
            list.remove(list[k])
print(list)

# 2
# numbers=[2,2,4,6,3,4,6]
# unique=[]
# for number in numbers:
#     if number not in unique:
#         print (number)
#         unique.append(number)
# print(unique)
