# https://leetcode.com/problems/car-pooling/description/
"""
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 

Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
"""
# Bucket Sort with notice that there are less than 1000 stops
from collections import defaultdict
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp = [0] * 1001
        for cost, src, dst in trips:
            timestamp[src] += cost
            timestamp[dst] -= cost
        used_capacity = 0
        for i in range(1001):
            passenger_change = timestamp[i]
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False
        return True

# O(n * log(n))
class SolutionSorting:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # create an array of timestamps [(time, passenger_change)]
        # [(source_time, + some passenger)], [(des_time, - some passenger)]
        timestamp = []
        for passenger_change, source, dest in trips:
            timestamp.append((source, passenger_change))
            timestamp.append((dest, -passenger_change))

        # sort the timestamp array based on time, and second sort key is passenger_change
        # when two timestamp has equal time, the smaller passenger_change will be prioritized
        # we always priority negative value, so at any time, unloading passengers
        # with negative passenger_change will be first evaluated
        timestamp.sort()

        used_capacity = 0
        for time, passenger_change in timestamp:
            used_capacity += passenger_change
            if used_capacity > capacity:
                return False

        return True

class SolutionBruteForce:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # trips = [[2, 0, 6], [3, 4, 10], [1, 5, 7], [2, 6, 8]]
        # capacity = 5
        # sort all trips based on source (from)
        max_number = 0
        for trip in trips:
            max_number = max(max_number, trip[2])

        graph = defaultdict(int)
        for trip in trips:
            cost, source, des = trip
            for i in range(source, des):
                graph[i] += cost

        for i in range(max_number + 1):
            if graph[i] > capacity:
                return False
        return True
