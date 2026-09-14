class Solution:
    def trap(self, height: List[int]) -> int:
        map_left = {}
        map_right = {} 
        
        max_left = 0
        max_right = 0

        # calc max left for each index
        for i, h in enumerate(height): 
            map_left[i] = max_left
            
            if h >= max_left:
                max_left = h

        # calc max right for each index
        for i in range(len(height)): 
            idx = (len(height) - 1) - i
            map_right[idx] = max_right

            if height[idx] >= max_right:
                max_right = height[idx]

        # print(map_left)
        # print(map_right)
        ans = 0
        for i, h in enumerate(height):
            # print(i, min(map_left[i], map_right[i]) - h)
            if min(map_left[i], map_right[i]) - h > 0:
                ans += min(map_left[i], map_right[i]) - h

        return ans

        