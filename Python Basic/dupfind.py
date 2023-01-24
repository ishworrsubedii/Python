sentence="I Love Nepaeeel".upper()

sentence2=sorted(list(set(sentence.upper())))
print(sentence2)
# x=sentence2.pop()
# print(x)
word_count = 0
for count in sentence:
    word_count += len(count)
print(word_count)
j=0
for i in sentence:
    z=sentence.count(i)
    print(z)
    if z>1:
       print(z)





 
# duplicate={}
# for i in sentence:
#     if sentence.count(i)>1:
#         if i not in duplicate:
#             duplicate.append(i)
# print(duplicate)
# for j in sentence:
#     count=sentence.count(duplicate)
#     print(j)
