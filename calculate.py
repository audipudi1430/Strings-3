class Solution:
    def calculate(self, s: str) -> int:
        """
        Approach:
        1. Traverse the string character by character to build numbers and track the current operation.
        2. Apply each operation based on the previous one: for '+' and '-', directly add/subtract; for '*' and '/', adjust the previous value in result.
        3. Use `prev` to hold the last computed value to correctly apply multiplication/division with precedence.

        Time Complexity: O(n), where n = len(s), since we process each character once.
        Space Complexity: O(1), no extra data structures used except a few integer variables.
        """

        i = 0
        res = prev = cur = 0
        operation = '+'

        while i < len(s):
            char = s[i]

            if char.isdigit():
                while i < len(s) and s[i].isdigit():
                    cur = cur * 10 + int(s[i])
                    i += 1
                i -= 1

                if operation == '+':
                    res += cur
                    prev = cur
                elif operation == '-':
                    res -= cur
                    prev = -cur
                elif operation == '*':
                    res -= prev
                    res += prev * cur
                    prev = prev * cur
                else:  # operation == '/'
                    res -= prev
                    res += int(prev / cur)  # integer division truncates toward zero
                    prev = int(prev / cur)

                cur = 0
            elif char != ' ':
                operation = char

            i += 1

        return res
