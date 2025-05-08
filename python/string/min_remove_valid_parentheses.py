# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
# related: # https://leetcode.com/problems/remove-invalid-parentheses/description/
"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 

Constraints:

1 <= s.length <= 105
s[i] is either '(' , ')', or lowercase English letter.
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # stack will always contains only one or multiple of "("
        # stack will not contains any ")" at all
        stack = []
        closing_to_remove = set()
        for i, ch in enumerate(s):
            if ch not in "()":
                continue
            elif ch == "(":
                stack.append(i)
            else:
                # ch == ")" now
                if not stack:
                    # illegal closing ")", when there is no opening "("
                    closing_to_remove.add(i)
                else:
                    # stack will have opening "(" at the top
                    # all previous couples of "(" and ")" has cancelled each another
                    stack.pop()
        # at this point, stack will contains the extra unneeded opening "("
        # indexes_to_remove contains all illegal closing ")"
        removed_indexes = closing_to_remove.union(set(stack))
        string_builder = []
        for i, c in enumerate(s):
            if i not in removed_indexes:
                string_builder.append(c)
        return "".join(string_builder)

class SolutionTwoRounds:
    def minRemoveToMakeValid(self, s: str) -> str:
        # keep a count, when meeting (, count += 1
        # case 1: lee(t(c)o)de)
        # case 2: ))abc(de), if we meet ")" before a "(", remove ")" as maintain count >= 0
        # case 3: at the end, if count = 0, we do not need to remove anything
        # case 4: if count > 0, we need to remove count number of "("
        # abc()()((, count = 2, we can remove 2 opening bracket "(" at the end

        # first round, find indexes of illegal ")", as case2 above
        count = 0
        step1 = []
        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                count += 1
            elif ch == ")":
                if count == 0:
                    # illegal closing bracket
                    # ignore this closing bracket and move to next iteration. do not update count
                    continue
                else:
                    count -= 1
            step1.append(ch)
        # new_s has been removed of illegal closing brackets
        new_s = "".join(step1)
        if count == 0:
            # the number of "(" is equal to ")"
            return new_s

        # the number of "(" is more than enough
        # remove count number of "(" from the end
        result = []
        for i in range(len(new_s) - 1, -1, -1):
            ch = new_s[i]
            if ch == "(" and count > 0:
                count -= 1
            else:
                result.append(ch)
        result = result[::-1]  # reverse the string
        return "".join(result)

import pytest  # noqa: E402

@pytest.fixture(params=[Solution, SolutionTwoRounds], ids=["StackSolution", "TwoRoundsSolution"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def test_example1(solution_instance):
    """Input: s = 'lee(t(c)o)de)' -> Output: 'lee(t(c)o)de'"""
    s = "lee(t(c)o)de)"
    expected = {"lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"}
    result = solution_instance.minRemoveToMakeValid(s)
    assert result in expected

def test_example2(solution_instance):
    """Input: s = 'a)b(c)d' -> Output: 'ab(c)d'"""
    s = "a)b(c)d"
    expected = "ab(c)d"
    assert solution_instance.minRemoveToMakeValid(s) == expected

def test_example3(solution_instance):
    """Input: s = '))((' -> Output: ''"""
    s = "))(("
    expected = ""
    assert solution_instance.minRemoveToMakeValid(s) == expected

def test_no_parentheses(solution_instance):
    """Input: s = 'abcde' -> Output: 'abcde'"""
    s = "abcde"
    expected = "abcde"
    assert solution_instance.minRemoveToMakeValid(s) == expected

def test_only_opening_parentheses(solution_instance):
    """Input: s = '(((abc' -> Output: 'abc'"""
    s = "(((abc"
    expected = "abc"
    assert solution_instance.minRemoveToMakeValid(s) == expected

def test_only_closing_parentheses(solution_instance):
    """Input: s = 'abc)))' -> Output: 'abc'"""
    s = "abc)))"
    expected = "abc"
    assert solution_instance.minRemoveToMakeValid(s) == expected

def test_nested_parentheses(solution_instance):
    """Input: s = '(a(b(c)d)e)' -> Output: '(a(b(c)d)e)'"""
    s = "(a(b(c)d)e)"
    expected = "(a(b(c)d)e)"
    assert solution_instance.minRemoveToMakeValid(s) == expected

def test_empty_string(solution_instance):
    """Input: s = '' -> Output: ''"""
    s = ""
    expected = ""
    assert solution_instance.minRemoveToMakeValid(s) == expected

def test_all_parentheses(solution_instance):
    """Input: s = '((()))' -> Output: '((()))'"""
    s = "((()))"
    expected = "((()))"
    assert solution_instance.minRemoveToMakeValid(s) == expected

def test_all_invalid_parentheses(solution_instance):
    """Input: s = '))))((((' -> Output: ''"""
    s = "))))(((("
    expected = ""
    assert solution_instance.minRemoveToMakeValid(s) == expected

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest