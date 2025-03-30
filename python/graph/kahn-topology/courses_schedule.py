# https://leetcode.com/problems/course-schedule-ii/description/
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # in-degree queue for keeping track of courses, which has no longer haved prerequisites
        q = deque()
        # courses that dependennt on this node as key, [node, set[dependent courses]]
        dependencies_dict = defaultdict(set)
        # courses that i have to take, before i can take node, [node, set[prerequisites]]
        prerequisites_dict = defaultdict(set)
        # finding out the inner nodes, which have no prerequisites
        for course, prev_course in prerequisites:
            prerequisites_dict[course].add(prev_course)
            dependencies_dict[prev_course].add(course)
        for course in range(numCourses):
            if len(prerequisites_dict[course]) == 0:
                q.append(course)

        result = list()
        # traversing the courses and make sure 
        while q:
            # this node is now free
            node = q.popleft()
            result.append(node)

            # check all dependencies of node
            for next_course in dependencies_dict[node]:
                prerequisites_dict[next_course].discard(node)
                # check if some neighbor courses are ready to be taken
                if len(prerequisites_dict[next_course]) == 0:
                    q.append(next_course)

                # may not be needed:
                # dependencies[node].discard(next_course)

        return result if len(result) == numCourses else []