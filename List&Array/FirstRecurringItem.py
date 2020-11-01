def rec(input):
    map = {}
    for i in range(len(input)):
        # print('i',i)
        # if input[i] in map.keys():
        if map.get(input[i]) or map.get(input[i])==0:
            return input[i]
        else:
            map[input[i]] = i
        # print('map',map)
    return None

# print(rec([1,2,5,2,3,4,5,5]))

def rec1(input):
    for i in range(len(input)):
        for j in range(1,len(input)):
            if input[i] == input[j]:
                return input[i]
    return None

print(rec1([1,2,1,2,3,4,5,5]))
