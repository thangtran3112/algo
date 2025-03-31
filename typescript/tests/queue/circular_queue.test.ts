import { MyCircularQueue } from '../../src/queue/circular_queue';

describe('MyCircularQueue', () => {
    test('should initialize correctly', () => {
        const queue = new MyCircularQueue(3);
        expect(queue.isEmpty()).toBe(true);
        expect(queue.isFull()).toBe(false);
        expect(queue.Front()).toBe(-1);
        expect(queue.Rear()).toBe(-1);
    });

    test('should handle enQueue operations', () => {
        const queue = new MyCircularQueue(3);

        // Add first element
        expect(queue.enQueue(1)).toBe(true);
        expect(queue.isEmpty()).toBe(false);
        expect(queue.isFull()).toBe(false);
        expect(queue.Front()).toBe(1);
        expect(queue.Rear()).toBe(1);

        // Add second element
        expect(queue.enQueue(2)).toBe(true);
        expect(queue.Front()).toBe(1);
        expect(queue.Rear()).toBe(2);

        // Add third element
        expect(queue.enQueue(3)).toBe(true);
        expect(queue.Front()).toBe(1);
        expect(queue.Rear()).toBe(3);
        expect(queue.isFull()).toBe(true);

        // Try to add when full
        expect(queue.enQueue(4)).toBe(false);
        expect(queue.Front()).toBe(1);
        expect(queue.Rear()).toBe(3);
    });

    test('should handle deQueue operations', () => {
        const queue = new MyCircularQueue(3);

        // Try to dequeue from empty queue
        expect(queue.deQueue()).toBe(false);

        // Add and then dequeue
        queue.enQueue(1);
        queue.enQueue(2);
        queue.enQueue(3);

        expect(queue.deQueue()).toBe(true);
        expect(queue.Front()).toBe(2);
        expect(queue.Rear()).toBe(3);
        expect(queue.isFull()).toBe(false);

        expect(queue.deQueue()).toBe(true);
        expect(queue.Front()).toBe(3);
        expect(queue.Rear()).toBe(3);

        expect(queue.deQueue()).toBe(true);
        expect(queue.isEmpty()).toBe(true);
        expect(queue.Front()).toBe(-1);
        expect(queue.Rear()).toBe(-1);

        // Try to dequeue from empty queue again
        expect(queue.deQueue()).toBe(false);
    });

    test('should handle circular behavior', () => {
        const queue = new MyCircularQueue(3);

        // Fill the queue
        queue.enQueue(1);
        queue.enQueue(2);
        queue.enQueue(3);

        // Remove from front
        expect(queue.deQueue()).toBe(true);

        // Add to rear (circular behavior)
        expect(queue.enQueue(4)).toBe(true);
        expect(queue.Front()).toBe(2);
        expect(queue.Rear()).toBe(4);

        // Continue cycling
        expect(queue.deQueue()).toBe(true); // Remove 2
        expect(queue.deQueue()).toBe(true); // Remove 3
        expect(queue.Front()).toBe(4);
        expect(queue.Rear()).toBe(4);

        expect(queue.deQueue()).toBe(true); // Remove 4
        expect(queue.isEmpty()).toBe(true);
    });

    test('should handle example from problem statement', () => {
        const myCircularQueue = new MyCircularQueue(3);
        expect(myCircularQueue.enQueue(1)).toBe(true);
        expect(myCircularQueue.enQueue(2)).toBe(true);
        expect(myCircularQueue.enQueue(3)).toBe(true);
        expect(myCircularQueue.enQueue(4)).toBe(false);
        expect(myCircularQueue.Rear()).toBe(3);
        expect(myCircularQueue.isFull()).toBe(true);
        expect(myCircularQueue.deQueue()).toBe(true);
        expect(myCircularQueue.enQueue(4)).toBe(true);
        expect(myCircularQueue.Rear()).toBe(4);
    });

    test('should handle edge case with capacity 1', () => {
        const queue = new MyCircularQueue(1);

        expect(queue.isEmpty()).toBe(true);
        expect(queue.isFull()).toBe(false);

        expect(queue.enQueue(5)).toBe(true);
        expect(queue.isEmpty()).toBe(false);
        expect(queue.isFull()).toBe(true);
        expect(queue.Front()).toBe(5);
        expect(queue.Rear()).toBe(5);

        expect(queue.enQueue(10)).toBe(false);
        expect(queue.deQueue()).toBe(true);
        expect(queue.isEmpty()).toBe(true);
        expect(queue.enQueue(15)).toBe(true);
        expect(queue.Front()).toBe(15);
        expect(queue.Rear()).toBe(15);
    });

    test('should handle multiple cycles of the circular queue', () => {
        const queue = new MyCircularQueue(3);

        // First cycle
        queue.enQueue(1);
        queue.enQueue(2);
        queue.enQueue(3);
        queue.deQueue();
        queue.deQueue();
        queue.deQueue();

        // Second cycle
        expect(queue.enQueue(4)).toBe(true);
        expect(queue.enQueue(5)).toBe(true);
        expect(queue.enQueue(6)).toBe(true);
        expect(queue.Front()).toBe(4);
        expect(queue.Rear()).toBe(6);

        // Partial dequeue and enqueue
        queue.deQueue(); // Remove 4
        expect(queue.enQueue(7)).toBe(true);
        expect(queue.Front()).toBe(5);
        expect(queue.Rear()).toBe(7);
    });

    test('should handle boundary values within constraints', () => {
        // Test with maximum capacity
        const largeQueue = new MyCircularQueue(1000);
        expect(largeQueue.isEmpty()).toBe(true);

        // Add maximum value
        expect(largeQueue.enQueue(1000)).toBe(true);
        expect(largeQueue.Rear()).toBe(1000);

        // Add minimum value
        largeQueue.deQueue();
        expect(largeQueue.enQueue(0)).toBe(true);
        expect(largeQueue.Rear()).toBe(0);
    });
});