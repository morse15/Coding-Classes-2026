# class Solution1:
#     def __init__(self,details):
#         self.details = details
#     def countSeniors(self):
#         tally = 0
#         for x in self.details:
#             age = int(x[11])
#             if age > 6:
#                 tally+=1
#             elif age == 6:
#                 age1 = int(x[12])
#                 if age1 > 0:
#                     tally+=1
#                 else:
#                     pass
#             else:
#                 pass
#         print(tally)
# a = Solution1(["1313579440F2036","2921522980M5644"])
# a.countSeniors()

# class Solution2:
#     def __init__(self,nums,target):
#         self.nums = nums
#         self.target = target
#     def twoSum(self):
#         list = []
#         for i in range(len(self.nums)):
#             for j in range(len(self.nums)):
#                 if i==j:
#                     pass
#                 elif (self.nums[i] + self.nums[j]) == self.target:
#                     list.append(i)
#                     list.append(j)
#                     print (list)
#                     break
# b = Solution2([4,5,6],10)
# b.twoSum()

# class Solution3:
#     def __init__(self,nums : list[int]) -> int:
#         self.nums = nums
#     def findMaxConsecutiveOnes(self):
#         tally = 0
#         tallyMax = 0
#         for x in range(len(self.nums)):
#             if self.nums[x]== 1:
#                 tally+=1
#                 if x == (len(self.nums)-1) and tally>tallyMax:
#                     if tally>tallyMax:
#                         tallyMax = tally
#             else:
#                 if tally>tallyMax:
#                     tallyMax = tally
#                 tally = 0
#         print(tallyMax)
# c = Solution3([1,1,0,1,1,1,0,1,0])
# c.findMaxConsecutiveOnes()

class Solution4:
    def __init__(self,strs : list[str]) -> str:
        self.strs = strs
    def longestCommonPrefix(self):
        longest = ""
        list = []
        for x in range(len(self.strs)):
            print(x)
            for y in range(len(self.strs[x])):
                print(y)
                

d = Solution4(["neet","feet"])
d.longestCommonPrefix()