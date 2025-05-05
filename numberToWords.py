class Solution:
    def numberToWords(self, num: int) -> str:
        """
        Approach:
        1. Split the number into chunks of 3 digits (thousands) and process each chunk individually.
        2. Use recursion (`helper`) to convert numbers < 1000 into words using predefined arrays for <20 and tens.
        3. For each chunk, append the appropriate thousand/million/billion suffix and build the final result.

        Time Complexity: O(log₁₀N), where N is the input number — each digit is processed once.
        Space Complexity: O(1), ignoring the output string — only fixed arrays and a few variables are used.
        """

        if num == 0:
            return "Zero"

        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                    "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
                    "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def helper(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + helper(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + helper(n % 100)

        res = ""
        i = 0

        while num > 0:
            if num % 1000 != 0:
                res = helper(num % 1000) + thousands[i] + " " + res
            num //= 1000
            i += 1

        return res.strip()
