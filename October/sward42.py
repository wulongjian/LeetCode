def maxSubArray(nums):
    temp = []
    temp.append(nums[0])
    for i in range(1, len(nums)):
        dp = temp[i-1]
        temp.append(max(dp+nums[i], nums[i]))
    return max(temp)



nums =  [-2,1,-3,4,-1,2,1,-5,4]
x = maxSubArray(nums)
print(x)
