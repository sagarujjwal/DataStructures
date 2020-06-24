#Find the largest pair sum in an unsorted array

# 1) Initialize both first and second largest
#    first = max(arr[0], arr[1])
#    second = min(arr[0], arr[1])
# 2) Loop through remaining elements (from 3rd to end)
#    a) If the current element is greater than first, then update first
#        and second.
#    b) Else if the current element is greater than second then update
#     second
# 3) Return (first + second)

def findLargestSumPair(arr, n):

    if arr[0] > arr[1]:
        first = arr[0]
        second = arr[1]
    else:
        first = arr[1]
        second = arr[0]

    for i in range(n):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]

    return first + second


arr=[100,2,33,4,5,6,77,9]
n=len(arr)
print ('Sum of max 2 pair is :',findLargestSumPair(arr, n))
