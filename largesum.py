def check_sum(arr):
    for num in arr:
        num_str = str(num)
        digits = set(num_str)
        print(digits)
        if len(digits) != len(num_str):
            return -1

    unique_sums = []
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            num1_str = str(arr[i])
            num2_str = str(arr[j])
            if len(set(num1_str + num2_str)) == len(num1_str) + len(num2_str):
                unique_sums.append(arr[i] + arr[j])

    if unique_sums is not None:
        return unique_sums
    else:
        return -1

array = [51, 176, 152, 57, 156]
result = check_sum(array)
print("Result:", result)



#two sum leet code

# def twoSum(nums,target):
#     i=0
#     for i in range(i,len(nums)):
#         for j in range(i+1,len(nums)):
#             if(nums[i]+nums[j]==target):
#                 return [i,j]
#     return[]
# nums=[2,7,3,8]
# target=9
# twoSum(nums,target)
