

# class Solution(object):
#     def numberOfSteps(self, num):
#         self.num = num
#         newnum = self.num
#         steps = 0
#         while newnum != 0:
#             if newnum % 2 == 0:
#                 newnum /= 2
#                 steps += 1
#             else:
#                 newnum -= 1
#                 steps += 1
#         return steps

# newnum = Solution()

# print(newnum.numberOfSteps(55))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # output = []
        # for i,val in enumerate(nums[:-1]):
        #     if nums[i] + nums[i + 1] == target:
        #         print(nums[i],nums[i+1])
        #         output.append(i)
        #         output.append(i+1)
        #         return output

        output = []
        for i,val in enumerate(nums):
            for e,val in enumerate(nums):
                if e != i:
                    if nums[i] + nums[e] == target:
                        print(i)
                        print(e)
                        print(nums[i] + nums[e])
                        output.append(i)
                        output.append(e)
                        return output

new = Solution()
print(new.twoSum([3,2,4],6))
