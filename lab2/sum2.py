
def add(data, target):
    for i in range(len(data)-1):
        for j in range(i+1, len(data)):
            if data[i]+data[j] == target:
                return [i, j]
