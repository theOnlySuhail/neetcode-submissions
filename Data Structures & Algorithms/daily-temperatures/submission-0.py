class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [0]
        ans = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while len(st) and temperatures[i] > temperatures[st[-1]]:
                ans[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)

        return ans


