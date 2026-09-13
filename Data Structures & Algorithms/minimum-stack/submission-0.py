class MinStack:

    def __init__(self):
        self.st = []
        self.min_st = []
        self.min_val = 0

    def push(self, val: int) -> None:
        if not len(self.st):
            self.min_st.append(val)
        else:
            self.min_st.append(min(self.getMin(), val))

        self.st.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.min_st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min_st[-1]
