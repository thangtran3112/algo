# https://leetcode.com/problems/remove-invalid-parentheses/description/
# related: # https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
"""

# Level 0:         "()())()"               ← invalid
#               /    |    |   \   ...
# Level 1:  ")())()" "(())()" ...          ← some valid
from collections import deque
import pytest

class SolutionWithStack:
    def removeInvalidParentheses(self, s: str):
        # this can also be done with a stack of 2 elements
        def is_valid(s):
            stack = []
            for ch in s:
                if ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    # no corresponding opening bracket
                    if not stack:
                        return False
                    stack.pop()
                # ignore non-bracket character like 'a', 'b','c'. Do not add them to stack
            return not stack

        result = []
        visited = set()
        queue = deque([s])
        found = False

        while queue:
            current = queue.popleft()
            if current in visited:
                continue
            visited.add(current)

            if is_valid(current):
                result.append(current)
                found = True

            if found:
                continue  # Skip generating next level if valid string already found

            for i in range(len(current)):
                if current[i] not in ('(', ')'):
                    continue
                # next_str is the result of deleting current[i]
                next_str = current[:i] + current[i + 1:]
                queue.append(next_str)

        return result

# Level 0:         "()())()"               ← invalid
#               /    |    |   \   ...
# Level 1:  ")())()" "(())()" ...          ← some valid
class SolutionBFSCountBracket:
    def removeInvalidParentheses(self, s: str):
        # this can also be done with a stack of 2 elements
        def is_valid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        queue = deque([s])
        # must use visited to avoid processing an identical string
        # it is possible that after remove few brackets, same strings can appear
        # in different BFS paths
        visited = set()
        result = []
        found = False

        while queue:
            # layer traversal, skip next layer, if found valid removal
            for _ in range(len(queue)):
                curr_str = queue.popleft()
                if curr_str in visited:
                    continue
                visited.add(curr_str)
                if is_valid(curr_str):
                    found = True
                    # only try to find any variant string at this layer. skip next layer
                    result.append(curr_str)
                # explore next layer of not found
                if not found:
                    for i in range(len(curr_str)):
                        if curr_str[i] != ')' and curr_str[i] != '(':
                            # non-bracket, it could other English letter
                            continue
                        # remove bracket at i, and put the remaining string to queue
                        queue.append(curr_str[:i] + curr_str[i + 1:])

        return result
    
