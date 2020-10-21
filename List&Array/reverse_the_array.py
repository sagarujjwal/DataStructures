# Function to reverse A[] from start to end
def reverseArray(list):
    output=[]
    for i in range(len(list)):
        output.append(list.pop())
    return output


# Recursive python program to reverse an array
def reverseListRecursive(list, start, end):
    if start >= end:
        return
    A[start], A[end] = A[end], A[start]
    # x=A[start]
    # A[start] = A[end]
    # A[end] = x
    reverseListRecursive(list, start+1, end-1)

# A = [1, 2, 3, 4, 5, 6]
# start = 0
# end = len(A)-1
# print(A)
# print(reverseListRecursive(A, start, end))
# print(A)

#time complexity O(n/2)
def reverse(list):
    for i in range(len(list)//2):
        a = list[i]
        list[i] = list[-i-1]
        list[-i-1] = a


A = [1, 2, 3, 4, 5, 6]
print(A)
print(reverse(A))
print(A)