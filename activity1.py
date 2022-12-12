lst = [8,3,5,1]
result = 0
length = len(lst)

for index in range(length):
    result += lst[index]*10**(length-
                              1-index)

print(result)
