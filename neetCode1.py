#No. 1
#establish ans outside the class as I use it twice and I didn't want to change anything about the variable of the class itself
ans = []
ans1=[]
class Solution1:
    def __init__(self,nums):
        self.nums = nums
    #first idea that came to my mind
    def getConcatenation(self):
        #as we need to do this twice, the range is 2
        for y in range(2):
            #adds every integer one by one
            for x in self.nums:
                ans.append(x)
        print(ans)
        #second idea that came to mind
    def Concatenate(self):
        #only primed to run twice, to make it easy to change would have to put it in a loop
        ans = self.nums[:]
        ans = ans + ans
        print(ans)
    def concatenateLoop(self):
        #I put it in a loop
        #alot more complicated than the first way, needs an extra variable, and doesn't do anything better than the original
        #but it works
        ans1 = self.nums[:]
        ans = self.nums[:]
        for z in range(1):
            ans += ans1
        print(ans)
#a = Solution1([1,2,3,4,5])
#a.getConcatenation()
#a.Concatenate()
#a.concatenateLoop()

#No. 2
class Solution2:
    def __init__(self,nums):
        self.nums = nums
    def hasDuplicate(self):
        copy = self.nums[:]
        for z in self.nums:
            copy.remove(z)
            if z in copy:
                check = True
                break
            else:
                check = False
            copy.append(z)
        print (check)
#b = Solution2([1,2,3,4])
#b.hasDuplicate()

#No. 3
class Solution3:
    def __init__(self,s,t):
        self.s = s
        #self.s = self.s.lower()
        self.t = t
        #self.t = self.t.lower()
    def isAnagram(self):
        if len(self.s) != len(self.t):
            print(False)
        else:
            print (sorted(self.s)==sorted(self.t))
#c = Solution3("racecar","carrace")
#c.isAnagram()

#No. 4
class Solution4:
    def __init__(self,arr):
        self.arr = arr
    def replaceElements(self):
        y = len(self.arr)
        for z in range(len(self.arr)):
            ans = []
            copy = self.arr[z:y]
            for x in copy:
                if self.arr[z] < x:
                    check = x
                    print(check)
            print(copy)
#d = Solution4([2,4,5,3,1,2])
#d.replaceElements()

dS = {}
dT = {}
s = "racecar"
t = "carrac"
for x in s:
    if x not in dS:
        dS[x] = 1
    else:
        dS[x] += 1

for y in t:
   if y not in dT:
       dT[y] = 1
   else:
       dT[y] += 1

for k,v in dS.items():
    if k in dT or dT[k] != v:
        print(False)
        break
    print(True)
# for z in t:
#     if z in d:
#         print(True)
#     else:
#         print(False)
print(dS)
print(dT)