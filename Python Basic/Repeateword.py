# from timeit import timeit #exceptiontimecount
# code=''' #exceptiontimecount
sentence = ("iiamdon")
list_upper_message = list(sentence.upper())
word_count = 0
count=len(sentence)
duplicate = set(list_upper_message)
max_count=0
for i in list_upper_message:
    count = list_upper_message.count(i)
    if count > max_count:
        max_count=count
        value=""
        value+=i
print(value,max_count)

# ''' #exceptiontimecount
# print(timeit(code,number=1)) #exceptiontimecount