# https://leetcode.com/problems/reconstruct-itinerary/description/
"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

 

Example 1:


Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]
Example 2:


Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
 

Constraints:

1 <= tickets.length <= 300
tickets[i].length == 2
fromi.length == 3
toi.length == 3
fromi and toi consist of uppercase English letters.
fromi != toi
"""
from collections import defaultdict
import heapq
from typing import List
import pytest

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(graph[src], dst)  # min-heap to maintain lexical order

        result = []

        def visit(airport):
            while graph[airport]:
                next_dest = heapq.heappop(graph[airport])
                visit(next_dest)
            result.append(airport)

        visit("JFK")
        return result[::-1]

class Solution2:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Adjacency list where destinations are stored in a min-heap
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True): # Sort tickets to push onto heap correctly
            graph[src].append(dst) # Using list as stack for DFS

        route = []
        def visit(airport):
            # Visit destinations in reverse lexical order (because we use list as stack)
            while graph[airport]:
                next_destination = graph[airport].pop()
                visit(next_destination)
            # Add airport to route after visiting all destinations (post-order)
            route.append(airport)

        visit("JFK")
        # The route is built in reverse, so reverse it at the end
        return route[::-1]

# --- TEST CASES ---

@pytest.fixture(params=[Solution, Solution2], ids=["HeapDFS", "StackDFS"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

# --- Individual Test Functions ---

def test_example1(solution_instance):
    """Tests the first example from the LeetCode description."""
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    expected = ["JFK", "MUC", "LHR", "SFO", "SJC"]
    assert solution_instance.findItinerary(tickets) == expected

def test_example2_lexical_order(solution_instance):
    """Tests the second example, focusing on lexical order."""
    tickets = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    expected = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]
    assert solution_instance.findItinerary(tickets) == expected

def test_simple_cycle(solution_instance):
    """Tests a simple cycle starting and ending at JFK."""
    tickets = [["JFK", "NRT"], ["NRT", "JFK"]]
    expected = ["JFK", "NRT", "JFK"]
    assert solution_instance.findItinerary(tickets) == expected

def test_multiple_flights_from_jfk(solution_instance):
    """Tests lexical ordering when multiple flights depart from JFK."""
    tickets = [["JFK", "LHR"], ["JFK", "CDG"], ["CDG", "JFK"]] # CDG comes before LHR
    expected = ["JFK", "CDG", "JFK", "LHR"]
    assert solution_instance.findItinerary(tickets) == expected

def test_longer_chain(solution_instance):
    """Tests a longer linear itinerary."""
    tickets = [["JFK", "A"], ["A", "B"], ["B", "C"], ["C", "D"]]
    expected = ["JFK", "A", "B", "C", "D"]
    assert solution_instance.findItinerary(tickets) == expected

def test_multiple_tickets_same_route(solution_instance):
    """Tests using the same ticket route multiple times."""
    tickets = [["JFK", "A"], ["A", "JFK"], ["JFK", "B"], ["B", "JFK"], ["A", "C"], ["C", "A"]]
    # Expected trace: JFK->A, A->C, C->A, A->JFK, JFK->B, B->JFK
    expected = ["JFK", "A", "C", "A", "JFK", "B", "JFK"]
    assert solution_instance.findItinerary(tickets) == expected

def test_single_ticket(solution_instance):
    """Tests an itinerary with only one ticket."""
    tickets = [["JFK", "LAX"]]
    expected = ["JFK", "LAX"]
    assert solution_instance.findItinerary(tickets) == expected

def test_complex_lexical_choice(solution_instance):
    """Tests a scenario where an early choice affects later lexical order."""
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    # Path: JFK -> NRT -> JFK -> KUL (NRT is chosen over KUL first)
    expected = ["JFK","NRT","JFK","KUL"]
    assert solution_instance.findItinerary(tickets) == expected

def test_another_complex_case(solution_instance):
    """Another complex test case involving cycles and choices."""
    tickets = [["EZE","AXA"],["TIA","ANU"],["ANU","JFK"],["JFK","ANU"],["ANU","EZE"],["TIA","ANU"],["AXA","TIA"],["JFK","TIA"],["ANU","TIA"],["JFK","EZE"]]
    # Expected trace: JFK->ANU, ANU->EZE, EZE->AXA, AXA->TIA, TIA->ANU, ANU->JFK, JFK->TIA, TIA->ANU, ANU->TIA, TIA->EZE
    expected = ["JFK","ANU","EZE","AXA","TIA","ANU","JFK","TIA","ANU","TIA","EZE"]
    assert solution_instance.findItinerary(tickets) == expected