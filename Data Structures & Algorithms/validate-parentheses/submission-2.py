class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        op = ['(', '[', '{']
        types = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for x in s:
            if x in op:
                st.append(x)
            else:
                if len(st) and types[x] == st[-1]:
                    st.pop()
                else:
                    return False

        return len(st) == 0