def add(data, target):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i]+data[j] == target:
                return [i, j]

test1 = [[2, 7, 11, 15], 9]
print(test1[0], "target:", test1[1])
print(add(test1[0], test1[1]))
test2 = [[3, 2, 4], 6]
print(test2[0], "target:", test2[1])
print(add(test2[0], test2[1]))
test3 = [[3, 3], 6]
print(test3[0], "target:", test3[1])
print(add(test3[0], test3[1]))
