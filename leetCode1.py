def twoSum(nums, target):
    #:type nums: List[int]
    #:type target: int
    #:rtype: List[int]

    for x in range(len(nums)):
        for y in range(1,len(nums)):
            if (nums[x] + nums[y]) == target:
                return x,y

print(twoSum([1,2,3,4,5],6))
