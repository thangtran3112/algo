
# https://leetcode.com/problems/expression-add-operators/description/
"""
Given a string num that contains only digits and an integer target, return all possibilities to insert the binary operators '+', '-', and/or '*' between the digits of num so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.
Example 3:

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions that can be created from "3456237490" to evaluate to 9191.
 

Constraints:

1 <= num.length <= 10
num consists of only digits.
-231 <= target <= 231 - 1
"""
# Step-by-step evaluation of expression: "1+2*3*4*5"
# Using: total = total - prev + (prev * curr) for '*'

# | Step | Expression        | prev | curr | total                     |
# |------|-------------------|------|------|----------------------------|
# | 1    | "1"               | 1    | –    | 1                          |
# | 2    | "1+2"             | 2    | 2    | 1 + 2 = 3                  |
# | 3    | "1+2*3"           | 6    | 3    | 3 - 2 + (2 * 3) = 7        |
# | 4    | "1+2*3*4"         | 24   | 4    | 7 - 6 + (6 * 4) = 25       |
# | 5    | "1+2*3*4*5"       | 120  | 5    | 25 - 24 + (24 * 5) = 121   |
from typing import List
import pytest

class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        # prev is the previous calculation result
        # in case of +, or -. It will be the previous element
        # in case of *, next prev will prev * curr
        def search(index: int, expr: str, prev: int, total: int):
            if index == len(num):
                if total == target:
                    result.append(expr)
                return

            for i in range(index, len(num)):
                # avoid numbers with leading zeros
                # except for the single letter 0 at index, we avoid "01", "00", "012", etc.
                if i != index and num[index] == '0':
                    break

                # there could be a number of multiple index
                # Eg. nums = 234, target = 27. We can have "23+4" = 27
                curr_str = num[index:i + 1]
                curr = int(curr_str)

                if index == 0:
                    # first number (no operator before it)
                    search(i + 1, curr_str, curr, curr)
                else:
                    # +
                    plus_prev = curr
                    search(i + 1, expr + "+" + curr_str, plus_prev, total + curr)
                    # -
                    minius_prev = -curr
                    search(i + 1, expr + "-" + curr_str, minius_prev, total - curr)
                    # *
                    multiply_prev = prev * curr
                    multiply_total = total - prev + prev * curr
                    search(i + 1, expr + "*" + curr_str, multiply_prev, multiply_total)

        search(0, "", 0, 0)
        return result
    
