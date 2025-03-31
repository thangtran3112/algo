import { MinStack } from '../../src/stack/min_stack';

// npx jest tests/stack/min_stack.test.ts
describe('MinStack', () => {
    test('example from the problem statement', () => {
        const minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        expect(minStack.getMin()).toBe(-3);
        minStack.pop();
        expect(minStack.top()).toBe(0);
        expect(minStack.getMin()).toBe(-2);
    });

    test('empty stack initialization', () => {
        const minStack = new MinStack();
        expect(minStack.size()).toBe(0);
    });

    test('push and top operations', () => {
        const minStack = new MinStack();
        minStack.push(5);
        expect(minStack.top()).toBe(5);
        minStack.push(10);
        expect(minStack.top()).toBe(10);
    });

    test('push and pop operations', () => {
        const minStack = new MinStack();
        minStack.push(5);
        minStack.push(10);
        minStack.push(15);
        minStack.pop();
        expect(minStack.top()).toBe(10);
        minStack.pop();
        expect(minStack.top()).toBe(5);
    });

    test('getMin returns the minimum value', () => {
        const minStack = new MinStack();
        minStack.push(5);
        expect(minStack.getMin()).toBe(5);
        minStack.push(3);
        expect(minStack.getMin()).toBe(3);
        minStack.push(7);
        expect(minStack.getMin()).toBe(3);
    });

    test('getMin returns correct min after popping', () => {
        const minStack = new MinStack();
        minStack.push(5);
        minStack.push(3);
        minStack.push(7);
        minStack.pop(); // Remove 7
        expect(minStack.getMin()).toBe(3);
        minStack.pop(); // Remove 3
        expect(minStack.getMin()).toBe(5);
    });

    test('handling multiple occurrences of the minimum value', () => {
        const minStack = new MinStack();
        minStack.push(1);
        minStack.push(1);
        minStack.push(1);
        expect(minStack.getMin()).toBe(1);
        minStack.pop();
        expect(minStack.getMin()).toBe(1);
        minStack.pop();
        expect(minStack.getMin()).toBe(1);
    });

    test('with negative values', () => {
        const minStack = new MinStack();
        minStack.push(-5);
        minStack.push(-10);
        minStack.push(-3);
        expect(minStack.getMin()).toBe(-10);
        minStack.pop(); // Remove -3
        expect(minStack.getMin()).toBe(-10);
        minStack.pop(); // Remove -10
        expect(minStack.getMin()).toBe(-5);
    });

    test('min changes correctly after various operations', () => {
        const minStack = new MinStack();
        minStack.push(10);
        minStack.push(5);
        minStack.push(15);
        expect(minStack.getMin()).toBe(5);
        minStack.pop(); // Remove 15
        expect(minStack.getMin()).toBe(5);
        minStack.pop(); // Remove 5
        expect(minStack.getMin()).toBe(10);
    });

    test('with boundary values from constraints', () => {
        const minStack = new MinStack();
        const maxVal = Math.pow(2, 31) - 1;
        const minVal = -Math.pow(2, 31);

        minStack.push(maxVal);
        expect(minStack.getMin()).toBe(maxVal);
        minStack.push(minVal);
        expect(minStack.getMin()).toBe(minVal);
    });

    test('a large number of operations', () => {
        const minStack = new MinStack();
        // Testing with a smaller number for test speed
        const numOperations = 1000;

        for (let i = 0; i < numOperations; i++) {
            minStack.push(i);
            expect(minStack.top()).toBe(i);
            expect(minStack.getMin()).toBe(0);
        }

        for (let i = numOperations - 1; i >= 0; i--) {
            expect(minStack.top()).toBe(i);
            minStack.pop();
        }
    });

    test('a complex sequence of operations', () => {
        const minStack = new MinStack();

        // Push values in decreasing then increasing order
        minStack.push(9);
        minStack.push(7);
        minStack.push(5);
        minStack.push(3);
        minStack.push(1);
        minStack.push(2);
        minStack.push(4);
        minStack.push(6);
        minStack.push(8);
        minStack.push(10);

        // Check current state
        expect(minStack.top()).toBe(10);
        expect(minStack.getMin()).toBe(1);

        // Remove some values
        minStack.pop(); // Remove 10
        minStack.pop(); // Remove 8
        minStack.pop(); // Remove 6

        // Check state
        expect(minStack.top()).toBe(4);
        expect(minStack.getMin()).toBe(1);

        // Remove the min
        minStack.pop(); // Remove 4
        minStack.pop(); // Remove 2
        minStack.pop(); // Remove 1

        // Check new min
        expect(minStack.getMin()).toBe(3);
    });
});