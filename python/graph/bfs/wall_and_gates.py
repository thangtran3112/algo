# https://leetcode.com/problems/walls-and-gates/
"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.
"""

from collections import deque
from typing import List

class SolutionMultiSourceBFS:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        EMPTY = 2147483647
        GATE = 0
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        if not rooms or not rooms[0]:
            return

        m, n = len(rooms), len(rooms[0])
        q = deque()

        # Find all gates
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == GATE:
                    q.append((row, col))
        
        # BFS from all gates
        # We search all rooms of distance d before rooms of distance (d+1), 
        # Therefore, the distance to an empty room must already be the shortest.
        while q:
            row, col = q.popleft()
            for row_direction, col_direction in DIRECTIONS:
                r, c = row + row_direction, col + col_direction
                if r < 0 or c < 0 or r >= m or c >= n or rooms[r][c] != EMPTY:
                    continue
                rooms[r][c] = rooms[row][col] + 1
                q.append((r, c))


# This is a single-source bfs, where we try each gate in sequence
# This can be optimized by using multiple-source BFS
class SolutionSingleSourceBFS:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        row_limit = len(rooms)
        col_limit = len(rooms[0])
        # find all gates and walls
        gates = list()
        walls = set()
        for row in range(row_limit):
            for col in range(col_limit):
                cell = rooms[row][col]
                pos_tuple = (row, col)
                if cell == -1:
                    walls.add(pos_tuple)
                    continue
                if cell == 0:
                    gates.append(pos_tuple)
                    continue

        # Empty room could have value of INF or the positive value from previous calculation
        # if meeting a new gate, we stop traversing, as the new gate will be nearer to future empty rooms
        def getAdjacentEmptyRooms(row, col) -> List:
            res = list()
            # below
            if (row - 1 >= 0) and rooms[row - 1][col] > 0:
                res.append((row - 1, col))
            # above
            if (row + 1 < row_limit) and rooms[row + 1][col] > 0:
                res.append((row + 1, col))
            # left
            if (col - 1 >= 0) and rooms[row][col - 1] > 0:
                res.append((row, col - 1))
            # right
            if (col + 1 < col_limit) and rooms[row][col + 1] > 0:
                res.append((row, col + 1))
            return res

        def processGate(gate_row, gate_col):
            step = 0
            q = deque()
            # start from a gate with step = 0
            q.append((gate_row, gate_col))
            visited = set()

            while q:
                size = len(q)

                # process this layer only
                for _ in range(size):
                    cur_row, cur_col = q.popleft()
                    empty_rooms = getAdjacentEmptyRooms(cur_row, cur_col)
                    for room in empty_rooms:
                        if room in visited:
                            continue
                        visited.add(room)
                        room_row, room_col = room
                        current_val = rooms[room_row][room_col]
                        new_val = min(current_val, step + 1)
                        # only update the room value, if we have a better route
                        if (new_val < current_val):
                            rooms[room_row][room_col] = new_val
                            # next layer processing
                            q.append((room_row, room_col))
                step += 1


        # navigate from each gates and update the rooms with minimum steps 
        for gate in gates:
            row, col = gate
            processGate(row, col)