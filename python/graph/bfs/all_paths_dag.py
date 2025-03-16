# https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/3853/
# BFS, space complexity (2^V * V), not the best for this question
# BFS is more efficient to find the shortest path
# This graph is a guaranteed DAG, there will be no cycle
# We do not need to keep track of visited nodes
import collections
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        n = len(graph)
        destination = n - 1
        if not graph or n == 0:
            return []
        path = [0]
        queue = collections.deque()
        queue.append(path)

        # keep and build the whole path in the queue
        # queue = [[node_0, node_1,...], [node_0, node_2, ...]]
        while queue:
            cur_path = queue.popleft()
            # last node in the path will be computed
            cur_node = cur_path[-1]
            if cur_node == destination:
                result.append(cur_path)
                continue
            for neighbor in graph[cur_node]:
                clone_path = list(cur_path)
                clone_path.append(neighbor)
                # append to the end of queue, not the front
                queue.append(clone_path)

        return result