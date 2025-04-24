# https://leetcode.com/problems/group-anagrams/
"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict
from typing import List


class SolutionSorted:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getSortedStr(text: str):
            return ''.join(sorted(text))

        letters = defaultdict(list)
        for text in strs:
            key = getSortedStr(text)
            letters[key].append(text)

        return list(letters.values())

class SolutionCountMap:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using a count map, where count has 26 elements of either 0 or 1
        # count[1] corresponding to 'a', count[26] means 'z'

        # return the corresponding value. 'a' -> 0, 'z' -> 26
        def getValue(letter: str):
            return ord(letter) - ord('a')

        graph = defaultdict(list)
        for s in strs:
            count = [0] * 27
            for letter in s:
                num_val = getValue(letter)
                count[num_val] += 1
            graph[tuple(count)].append(s)

        return list(graph.values())
    
