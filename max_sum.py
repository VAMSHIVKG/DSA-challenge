def max_sum(arr):
    maxsum=-1
    for i in range(len(A)):
        for j in range (i+1,len(A)):
            # nums=[A[i],A[j]]
            if not num_str[i].intersection(num_str[j]):
                cur_sum=A[i]+A[j]
                # nums=[A[i],A[j]]
                if cur_sum>maxsum:
                    maxsum=cur_sum
                    nums=[A[i],A[j]]
    print(nums)
    return maxsum
    # print(maxsum)
A=[51,23,56,173,6,35]
num_str=[set(str(item))for item in A]
result=max_sum(A)
print(result)

