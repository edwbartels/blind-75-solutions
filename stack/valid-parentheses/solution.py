class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_open = ["(", "[", "{"]
        valid_close = [")", "]", "}"]
        for char in s:
            if char not in valid_open + valid_close:
                return False
            if char in valid_open:
                stack.append(char)
            elif char in valid_close:
                if stack:
                    if valid_open[valid_close.index(char)] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) != 0:
            return False
        return True
