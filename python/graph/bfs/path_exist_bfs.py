# https://leetcode.com/problems/find-if-path-exists-in-graph/
import collections
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        visited[source] = True
        queue = collections.deque([source])

        while queue:
            # popleft() add element to the front, 0(1)
            cur_node = queue.popleft()
            if cur_node == destination:
                return True

            for neighbor in graph[cur_node]:
                if not visited[neighbor]:
                    # add element to the right (last element)
                    # use appendLeft() to attach to the front of the queue
                    queue.append(neighbor)
                    visited[neighbor] = True

        return False