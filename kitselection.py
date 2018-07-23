def findMinimum (arr):
    # Write code here
    n = len(arr)
    halfSum = 0
    for i in range(n):
        halfSum = halfSum + arr[i]
     
    halfSum = int(halfSum / 2)
     
    # sort the array in descending order.
    arr.sort(reverse = True)
     
    res = 0
    curr_sum = 0
    for i in range(n):
         
        curr_sum += arr[i]
        res += 1
 
        # current sum greater than sum
        if curr_sum > halfSum:
            return res
     
    return res

n = int(input())
arr = list(map(int, input().split()))

out_ = findMinimum(arr)
print (out_)
