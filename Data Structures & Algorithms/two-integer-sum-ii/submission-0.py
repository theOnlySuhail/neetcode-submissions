class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            y = target - numbers[l]
            if y == numbers[r]:
                return [l + 1, r + 1]
            elif y < numbers[r]:
                r -= 1
            else:
                l += 1
        