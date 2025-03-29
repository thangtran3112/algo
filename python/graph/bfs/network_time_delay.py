"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""
from collections import defaultdict, deque
from typing import List


class SolutionBFS:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_dict = defaultdict(list)
        infinity = float('inf')
        min_times = [0] + [infinity] * n

        for u, v, cost in times:
            adj_dict[u].append((cost, v))
        queue = deque()
        queue.append((0, k))

        while queue:
            travel_time, node = queue.popleft()
            if travel_time < min_times[node]:
                min_times[node] = travel_time
                for cost, adj_node in adj_dict[node]:
                    queue.append((travel_time + cost, adj_node))

        result = max(min_times)
        return result if result < infinity else -1