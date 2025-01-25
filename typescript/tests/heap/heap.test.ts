import { MinHeap } from '../../src/heap/heap';

describe('MinHeap', () => {
    let heap: MinHeap;

    beforeEach(() => {
        heap = new MinHeap();
    });

    test('should initialize empty heap', () => {
        expect(heap.isEmpty()).toBe(true);
        expect(heap.size()).toBe(0);
        expect(heap.getMin()).toBeUndefined();
    });

    test('should create heap from array', () => {
        heap = new MinHeap([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]);
        expect(heap.getMin()).toBe(1);
        expect(heap.getHeap()[0]).toBe(1);
    });

    test('should maintain heap property after insertions', () => {
        heap.insert(5);
        heap.insert(3);
        heap.insert(7);
        heap.insert(1);
        expect(heap.getMin()).toBe(1);
    });

    test('should extract minimum element', () => {
        heap = new MinHeap([3, 1, 4, 1, 5]);
        expect(heap.extractMin()).toBe(1);
        expect(heap.extractMin()).toBe(1);
        expect(heap.extractMin()).toBe(3);
    });

    test('should handle duplicate elements', () => {
        heap = new MinHeap([2, 2, 2, 2]);
        expect(heap.extractMin()).toBe(2);
        expect(heap.size()).toBe(3);
        expect(heap.getMin()).toBe(2);
    });

    test('should handle negative numbers', () => {
        heap = new MinHeap([-1, 5, -10, 0, 3]);
        expect(heap.extractMin()).toBe(-10);
        expect(heap.extractMin()).toBe(-1);
        expect(heap.extractMin()).toBe(0);
    });

    test('should maintain heap property after multiple operations', () => {
        heap.insert(3);
        heap.insert(1);
        heap.extractMin();
        heap.insert(2);
        heap.insert(0);
        expect(heap.extractMin()).toBe(0);
        expect(heap.extractMin()).toBe(2);
        expect(heap.extractMin()).toBe(3);
    });

    test('should handle extractMin on empty heap', () => {
        expect(heap.extractMin()).toBeUndefined();
    });

    test('should handle large number of elements', () => {
        const numbers = Array.from({ length: 100 }, (_, i) => i);
        heap = new MinHeap(numbers.reverse());
        expect(heap.getMin()).toBe(0);
        expect(heap.size()).toBe(100);
    });

    test('should maintain heap property after all elements removed', () => {
        heap = new MinHeap([3, 1, 4, 1, 5]);
        while (!heap.isEmpty()) {
            heap.extractMin();
        }
        expect(heap.size()).toBe(0);
        heap.insert(1);
        expect(heap.getMin()).toBe(1);
    });
});
