class Solution:
    def isValid(self, s: str) -> bool:
        bracket_elements = {']':'[', ')':'(', '}': '{'}
        stack = []
        for i in s:
            if i in bracket_elements:
                # FIX: Explicitly check stack before popping to avoid evaluation quirks
                if stack:
                    top_element = stack.pop()
                else:
                    top_element = "#"
                
                if bracket_elements[i] != top_element:
                    return False
            else:
                stack.append(i)
        return not stack

        