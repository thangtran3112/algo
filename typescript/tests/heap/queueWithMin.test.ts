import { QueueWithMin } from '../../src/heap/queueWithMin';

describe('QueueWithMin', () => {
    let queue: QueueWithMin;

    beforeEach(() => {
        queue = new QueueWithMin();
    });

    test('should initialize empty', () => {
        expect(queue.getMin()).toBeUndefined();
    });

    test('should handle single element operations', () => {
        queue.add(5);
        expect(queue.getMin()).toBe(5);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBeUndefined();
    });

    test('should track min with ascending values', () => {
        queue.add(1);
        queue.add(2);
        queue.add(3);
        expect(queue.getMin()).toBe(1);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(2);
    });

    test('should track min with descending values', () => {
        queue.add(3);
        queue.add(2);
        queue.add(1);
        expect(queue.getMin()).toBe(1);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(1);
    });

    test('should handle duplicates', () => {
        queue.add(2);
        queue.add(2);
        queue.add(2);
        expect(queue.getMin()).toBe(2);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(2);
    });

    test('should handle alternating min values', () => {
        queue.add(3);
        queue.add(1);
        queue.add(4);
        queue.add(1);
        expect(queue.getMin()).toBe(1);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(1);
    });

    test('should handle complex sequence with removals', () => {
        queue.add(5);
        queue.add(3);
        queue.add(3);
        queue.add(7);
        queue.removeFirstAdded();
        queue.add(2);
        expect(queue.getMin()).toBe(2);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(2);
    });

    test('should handle removing all elements', () => {
        queue.add(3);
        queue.add(2);
        queue.add(1);
        queue.removeFirstAdded();
        queue.removeFirstAdded();
        queue.removeFirstAdded();
        expect(queue.getMin()).toBeUndefined();
    });

    test('should handle add after empty', () => {
        queue.add(1);
        queue.removeFirstAdded();
        queue.add(2);
        expect(queue.getMin()).toBe(2);
    });

    test('should handle mixed duplicates and unique values', () => {
        queue.add(3);
        queue.add(3);
        queue.add(1);
        queue.add(3);
        expect(queue.getMin()).toBe(1);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(1);
    });

    test('should handle alternating add and remove', () => {
        queue.add(5);
        queue.removeFirstAdded();
        queue.add(3);
        queue.removeFirstAdded();
        queue.add(4);
        expect(queue.getMin()).toBe(4);
    });

    test('should handle same min after multiple operations', () => {
        queue.add(2);
        queue.add(3);
        queue.add(2);
        queue.removeFirstAdded();
        queue.add(4);
        expect(queue.getMin()).toBe(2);
    });

    test('should handle decreasing then increasing sequence', () => {
        queue.add(5);
        queue.add(4);
        queue.add(3);
        queue.add(4);
        queue.add(5);
        expect(queue.getMin()).toBe(3);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(3);
    });

    test('should handle rapid add/remove sequences', () => {
        queue.add(1);
        queue.removeFirstAdded();
        queue.add(2);
        queue.removeFirstAdded();
        queue.add(3);
        expect(queue.getMin()).toBe(3);
    });

    test('should handle large number of duplicates', () => {
        for (let i = 0; i < 5; i++) queue.add(1);
        expect(queue.getMin()).toBe(1);
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(1);
    });

    test('should handle min value changes after multiple removes', () => {
        queue.add(3);
        queue.add(1);
        queue.add(2);
        queue.add(1);
        queue.removeFirstAdded();
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(1);
    });

    test('should handle edge case with repeated min values', () => {
        queue.add(1);
        queue.add(2);
        queue.add(1);
        queue.removeFirstAdded();
        queue.add(1);
        expect(queue.getMin()).toBe(1);
    });

    test('should maintain correct min after multiple operations', () => {
        queue.add(5);
        queue.add(3);
        queue.removeFirstAdded();
        queue.add(4);
        queue.add(2);
        queue.removeFirstAdded();
        queue.add(1);
        expect(queue.getMin()).toBe(1);
    });

    test('should handle interleaved duplicates and unique values', () => {
        queue.add(2);
        queue.add(2);
        queue.add(1);
        queue.add(2);
        queue.add(1);
        queue.removeFirstAdded();
        queue.removeFirstAdded();
        expect(queue.getMin()).toBe(1);
    });
});
