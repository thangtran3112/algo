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
src != dst"
"""
from typing import List
"""
IMPORTANT:
- There is a limit on the number of edges/hops you can take from the source
- The Single shortest Faster Algorithm (SPFA) will not work, because there is no guarantee
  that we only cover k edges or k hops. It could go beyond k-hops
- In this case, we can only use the normal BellmanFord algorithm with DP
- We need to maintain 2 arrays costs and next_costs
- Important: previous computation on costs are not allowed to be mutated
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        infinity = float('inf')

        costs = [infinity] * n

        # start from src
        costs[src] = 0

        # k hops means k+1 edges. For instance: [1->2->3->4] only use 2 hops [2,3], and involves 3 edges
        for _ in range(k+1):
            # check for update, so we can early exit, if there is no update
            update = False
            # make a copy of previous costs, so we are not mutate the computation of previous layer
            # We are allowed to mutate next_costs in-place as we like
            next_costs = costs[:]

            for u,v, price in flights:
                # price could be negative, in case of costs[u] = infinity, we do not want to do (infinity + negative)
                # doing next_costs[v] = infinity + negative is risky, as it may create unwanted number
                if costs[u] != infinity and costs[u] + price < next_costs[v]:
                    # next_costs[v] may already be recomputed, do not use costs[v] for above comparison
                    update = True
                    next_costs[v] = costs[u] + price
                
            # check for early exist, if nothing changes compared to previous costs calculation
            if not update:
                break
            else:
                costs = next_costs

        result = costs[dst] if costs[dst] < infinity else -1
        return result