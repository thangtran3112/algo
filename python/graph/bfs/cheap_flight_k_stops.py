# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
"""
There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

 

Example 1:


Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.
Example 2:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.
Example 3:


Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
 

Constraints:

1 <= n <= 100
0 <= flights.length <= (n * (n - 1) / 2)
flights[i].length == 3
0 <= fromi, toi < n
fromi != toi
1 <= pricei <= 104
There will not be any multiple flights between two cities.
0 <= src, dst, k < n
src != dst
"""
import collections
from typing import List


class SolutionBFS:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u,nei,cost in flights:
            adj[u].append((nei, cost))

        # unlike Dijkstra, we do not need a heap
        # (src, 0) mean (node, cost). We can use (node, cost, stop) too, but it is not necessary in BFS
        # BFS will always go through all nodes at the same level (stop), before exploring the next level (stop)
        # We just need a common stops variable to keep track of it
        q = collections.deque()
        q.append((src, 0))
        stops = 0

        infinity = float('inf')
        prev_costs = [infinity] * n
        prev_costs[src] = 0

        # there is max k+1 edges, when given k stops in between
        while stops < k+1 and q:
            # only processing the existing layer, even there will be next elements to be inserted
            size = len(q)
            # calculate the next-layer of shortest cost, without mutating the previous layer
            next_costs = prev_costs[:]
            # must traverse all node within the existing queue first, same layer processing
            for i in range(size):
                node, cost = q.popleft()
                for neighbor, nei_cost in adj[node]:
                    if cost + nei_cost < next_costs[neighbor]:
                        next_costs[neighbor] = cost + nei_cost
                        # append, but this new element will not be processed until next layer
                        q.append((neighbor, next_costs[neighbor]))

            # reassign prev_costs, after done processing a full layer. process to next layer
            prev_costs = next_costs
            stops += 1

        return -1 if prev_costs[dst] == infinity else prev_costs[dst]