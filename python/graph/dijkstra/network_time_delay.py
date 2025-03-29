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
from collections import defaultdict
import collections
import heapq
from typing import List


class SimplifiedDijkstra:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
                # [0, infinity]
        infinity = float("inf")
        # keep track of shortest time array for reaching from source node k
        travel_times = [0] + [infinity] * n
        graph = defaultdict(list)
        pq = [(0, k)]

        for src, des, w in times:
            graph[src].append((des, w))
        while pq:
            time, node = heapq.heappop(pq)
            # if the heap time to node less than current recorded total time to this node
            if time < travel_times[node]:
                travel_times[node] = time

                for adj_node, w in graph[node]:
                    heapq.heappush(pq, (time + w, adj_node))

        # we have an array of minimum cost to each node as travel_times
        best = max(travel_times)
        return best if best < infinity else -1

class EdgeRelaxationDijkstra:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # [0, infinity]
        infinity = float("inf")
        # keep track of shortest time array for reaching from source node k
        travel_times = [0] + [infinity] * n
        graph = defaultdict(list)
        pq = [(0, k)]

        # optional to use visited, to relax edge computation (Edge relaxation)
        visited = set()
        for src, des, w in times:
            graph[src].append((des, w))
        while pq:
            time, node = heapq.heappop(pq)
            # if the heap time to node less than current recorded total time to this node
            if time < travel_times[node]:
                travel_times[node] = time
                visited.add(node)

                if len(visited) == n:
                    break
                for adj_node, w in graph[node]:
                    if adj_node not in visited:
                        heapq.heappush(pq, (time + w, adj_node))

        # we have an array of minimum cost to each node as travel_times
        best = max(travel_times)
        return best if best < infinity else -1
    
# Solution with not keeping track of shortest travel time to each node
# Stop the calculation, right when visited all n nodes
# Keeptrack of total_time in heap only
class SimplifiedEdgeRelaxDijkstra:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Group all edges by source node into a dict[src, list(time)], time=(cost, des)
        # results will be a list of tuple (destination, cost, previous_node)
        # intially, we set (k, 0, k) for the starting node
        # start traversing from all edges from k in the dict
        # keep a visited set
        adj_dict = collections.defaultdict(list)
        for src, des, cost in times:
            # keep cost as the first element, so the heap will use it for sorting
            adj_dict[src].append((cost, des))
        
        visited = set()
        pq = [(0, k)]

        while pq:
            travel_time, node = heapq.heappop(pq)
            visited.add(node)

            # Early escape, edge relax
            if len(visited) == n:
                return travel_time

            # for all adjacent nodes, update the heap with possible next total travel time
            for edge in adj_dict[node]:
                # (des, cost) tuple
                cost, adj_node = edge
                if adj_node not in visited:
                    next_tuple = (travel_time + cost, adj_node)
                    heapq.heappush(pq, next_tuple)

        # there are unreachable node from source k
        return -1