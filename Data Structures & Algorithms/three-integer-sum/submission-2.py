class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            target = -nums[i]
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                # if l == i:
                #     l += 1
                #     continue
                # elif r == i:
                #     r -= 1
                #     continue

                y = target - nums[l]
                if y == nums[r]:
                    output.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                    # break
                elif y < nums[r]:
                    r -= 1
                else:
                    l += 1

        return output
