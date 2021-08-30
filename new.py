

class Solution(object):
    def numberOfSteps(self, num):
        self.num = num
        newnum = self.num
        steps = 0
        while newnum != 0:
            if newnum % 2 == 0:
                newnum /= 2
                steps += 1
            else:
                newnum -= 1
                steps += 1
        return steps

newnum = Solution()

print(newnum.numberOfSteps(55))