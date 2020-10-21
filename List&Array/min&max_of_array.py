#Find the maximum and minimum element in an array
def minmaxArray(list):
    x = list[0]
    y = list[1]
    if x>y:
        max=x
        min=y
    else:
        max=y
        min=x
    for i in range(2,len(list)):
        if max < list[i]:
            max= list[i]
        elif min > list[i]:
            min=list[i]
    return min,max

A = [-1,9,0,1, 2, 3, 4, 5, 6,-99]
print(minmaxArray(A))