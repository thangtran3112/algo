# https://leetcode.com/problems/min-stack/description/
"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            new_tuple = (val, val)
            self.stack.append(new_tuple)
            return

        # (val, current_min)
        prev_tuple = self.stack[len(self.stack) - 1]
        prev_min = prev_tuple[1]

        if val < prev_min:
            new_tuple = (val, val)
            self.stack.append(new_tuple)
            return

        new_tuple = (val, prev_min)
        self.stack.append(new_tuple)


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return -1
        # (val, current_min)
        cur_tuple = self.stack[len(self.stack) - 1]
        return cur_tuple[0]

    def getMin(self) -> int:
        # (val, current_min)
        cur_tuple = self.stack[len(self.stack) - 1]
        return cur_tuple[1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()