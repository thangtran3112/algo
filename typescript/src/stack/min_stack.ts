// https://leetcode.com/problems/min-stack/
/**
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
 */

class Tuple {
    val: number;
    min: number;

    constructor(val: number, min: number) {
        this.val = val;
        this.min = min;
    }
}

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export class MinStack {
    array: Tuple[];
    constructor() {
        this.array = [];
    }

    size(): number {
        return this.array.length;
    }

    push(val: number): void {
        let newMin = val;
        if (this.size() > 0) {
            const prev_tuple = this.array[this.size() - 1];
            newMin = Math.min(prev_tuple.min, val);
        }
        const newTuple = new Tuple(val, newMin);
        this.array.push(newTuple);
    }

    pop(): void {
        this.array.pop();
    }

    top(): number {
        if (this.size() > 0) {
            return this.array[this.size() - 1].val;
        }
        return Infinity;
    }

    getMin(): number {
        if (this.size() > 0) {
            return this.array[this.size() - 1].min;
        }
        return Infinity;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */