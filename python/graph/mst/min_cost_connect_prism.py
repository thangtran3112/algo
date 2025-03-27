import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # Min heap to store the edges 
        pq = [(0,0)]  # (cost, point index), cost to visit 0 is 0

        # To keep track of visited points
        visited = [False] * n

        mst_cost = 0
        edges_used = 0

        while edges_used < n:
            cost, node = heapq.heappop(pq)
            
            # If not was already in MST, we discard this edge
            if visited[node]:
                continue

            # not visited yet
            visited[node] = True
            mst_cost += cost
            edges_used += 1

            # Add all unvisited edges from the current node to the heap
            for next_node in range(n):
                if not visited[next_node]:
                    next_cost = abs(points[node][0] - points[next_node][0]) + abs(points[node][1] - points[next_node][1])
                    heapq.heappush(pq, (next_cost, next_node))

        return mst_cost