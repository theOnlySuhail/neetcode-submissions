class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            try:
                st.append(int(token))
            except:
                num2 = st.pop()
                num1 = st.pop()
                print(f'num1: {num1}, num2: {num2}')
                result = self.apply_op(token, num1, num2)
                st.append(result)

        return st[-1]



    def apply_op(self, op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            return int(a / b)
            

