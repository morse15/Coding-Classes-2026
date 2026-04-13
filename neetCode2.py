#No. 1
class Solution1:
    def __init__(self,s,t):
        self.s = s
        self.t = t
    def isSubsequence(self):
        if self.t not in self.s:
            print(False)
        else:
            for character in self.t:
                print("yes")

#No. 2
# values = {}
# score = 0
# for y in "abcdefghijklmnopqrstuvwxyz":
#     score += 1
#     values[y] = score + 96
# print(values)
    
class Solution2:
    def __init__(self,s):
        self.s = s
    def scoreOfString(self):
        values = [ord(character) for character in reversed(self.s)]
        sub = []
        answer = 0
        for point in range((len(values))-1):
            x = abs(values[point] - values[point+1])
            sub.append(x)
        for point in sub:
            answer += point
        print(answer)

b = Solution2("neet")
b.scoreOfString()

#No. 3
class Solution3:
    def __init__(self,s):
          self.s = s
    def lengthOfLastWord(self):
        length = 0
        for z in self.s:
            if z == " ":
                length = 0
            else:
                length += 1
                lengthReal = length
        print(lengthReal)

c = Solution3("one two three one")
c.lengthOfLastWord()

# def string_to_ascii (string: str):
#     characters = list(string)
#     scores     = [ord(character) for character in characters]
#     return scores

# def difference_scores (scorelist: list):
#     max        = len(scorelist)
#     new_scores = []
#     for score in scorelist:
#         index_of_next = scorelist.index(score) + 1
#         if index_of_next <= max:
#             next_item     = scorelist[index_of_next]
#         else:
#             next_item = 0
#         new_score = score - next_item
#         new_scores.append(new_score)
#     return new_scores

# def stringtodifference(string: str):
#     scores       = string_to_ascii(reversed(string))
#     differences  = difference_scores(scores)
#     summed_score =  sum(scores)
#     return summed_score

# test = stringtodifference("code")
# print(test)


# scorelist          = [400, 300, 200, 100]
# differenced_scores = []
# window_start       = 0

# for score in scorelist:
#     window_start       += 1
#     window_size        = 2
#     window_end         = window_start + window_size - 1
#     element_indices    = range(window_start, (window_end if window_start <= len(scorelist) else window_start))
#     elements           = [scorelist[index] for index in element_indices]
#     difference         = elements[-1] - elements[0]
#     print(difference)
#     differenced_scores.append(difference)
