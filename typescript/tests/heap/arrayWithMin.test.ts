import { ArrayWithMin } from '../../src/heap/arrayWithMin';

describe('ArrayWithMin array contents', () => {
    let arrayWithMin: ArrayWithMin;

    beforeEach(() => {
        arrayWithMin = new ArrayWithMin();
    });

    test('should initialize with empty arrays', () => {
        expect(arrayWithMin.array).toEqual([]);
        expect(arrayWithMin.minArray).toEqual([]);
    });

    test('should add single element correctly', () => {
        arrayWithMin.add(5);
        expect(arrayWithMin.array).toEqual([5]);
        expect(arrayWithMin.minArray).toEqual([5]);
    });

    test('should track minimum when adding ascending values', () => {
        arrayWithMin.add(1);
        arrayWithMin.add(2);
        arrayWithMin.add(3);
        expect(arrayWithMin.array).toEqual([1, 2, 3]);
        expect(arrayWithMin.minArray).toEqual([1]);
        expect(arrayWithMin.getMin()).toBe(1);
    });

    test('should track minimum when adding descending values', () => {
        arrayWithMin.add(3);
        arrayWithMin.add(2);
        arrayWithMin.add(1);
        expect(arrayWithMin.array).toEqual([3, 2, 1]);
        expect(arrayWithMin.minArray).toEqual([3, 2, 1]);
        expect(arrayWithMin.getMin()).toBe(1);
    });

    test('should handle alternating min values', () => {
        arrayWithMin.add(3);
        arrayWithMin.add(1);
        arrayWithMin.add(4);
        arrayWithMin.add(2);
        expect(arrayWithMin.array).toEqual([3, 1, 4, 2]);
        expect(arrayWithMin.minArray).toEqual([3, 1]);
        expect(arrayWithMin.getMin()).toBe(1);
    });

    test('should handle adding same value multiple times then removing', () => {
        arrayWithMin.add(2);
        arrayWithMin.add(2);
        arrayWithMin.add(2);
        expect(arrayWithMin.minArray).toEqual([2, 2, 2]);
        arrayWithMin.removeLastAdded();
        expect(arrayWithMin.minArray).toEqual([2, 2]);
        expect(arrayWithMin.getMin()).toBe(2);
    });

    test('should handle adding decreasing then increasing values', () => {
        arrayWithMin.add(5);
        arrayWithMin.add(4);
        arrayWithMin.add(3);
        arrayWithMin.add(4);
        arrayWithMin.add(5);
        expect(arrayWithMin.array).toEqual([5, 4, 3, 4, 5]);
        expect(arrayWithMin.minArray).toEqual([5, 4, 3]);
        expect(arrayWithMin.getMin()).toBe(3);
    });

    test('should handle removing all elements', () => {
        arrayWithMin.add(3);
        arrayWithMin.add(2);
        arrayWithMin.add(1);
        arrayWithMin.removeLastAdded();
        arrayWithMin.removeLastAdded();
        arrayWithMin.removeLastAdded();
        expect(arrayWithMin.array).toEqual([]);
        expect(arrayWithMin.minArray).toEqual([]);
        expect(arrayWithMin.getMin()).toBeUndefined();
    });

    test('should handle complex sequence with duplicates', () => {
        arrayWithMin.add(5);
        expect(arrayWithMin.getMin()).toBe(5);
        arrayWithMin.add(5);
        arrayWithMin.add(3);
        expect(arrayWithMin.getMin()).toBe(3);
        arrayWithMin.removeLastAdded();
        expect(arrayWithMin.getMin()).toBe(5);
        arrayWithMin.add(4);
        arrayWithMin.add(5);
        expect(arrayWithMin.array).toEqual([5, 5, 4, 5]);
        expect(arrayWithMin.minArray).toEqual([5, 5, 4]);
    });

    test('should handle remove-then-add sequence', () => {
        arrayWithMin.add(3);
        arrayWithMin.add(2);
        arrayWithMin.removeLastAdded();
        arrayWithMin.add(1);
        arrayWithMin.removeLastAdded();
        arrayWithMin.add(4);
        expect(arrayWithMin.array).toEqual([3, 4]);
        expect(arrayWithMin.minArray).toEqual([3]);
        expect(arrayWithMin.getMin()).toBe(3);
    });

    test('should handle repeated same number with removals', () => {
        arrayWithMin.add(2);
        arrayWithMin.add(2);
        arrayWithMin.removeLastAdded();
        expect(arrayWithMin.array).toEqual([2]);
        arrayWithMin.add(2);
        arrayWithMin.add(2);
        arrayWithMin.removeLastAdded();
        expect(arrayWithMin.array).toEqual([2, 2]);
        expect(arrayWithMin.minArray).toEqual([2, 2]);
        expect(arrayWithMin.getMin()).toBe(2);
    });

    test('should handle large numbers and edge cases', () => {
        arrayWithMin.add(Number.MAX_SAFE_INTEGER);
        arrayWithMin.add(Number.MIN_SAFE_INTEGER);
        arrayWithMin.add(0);
        expect(arrayWithMin.getMin()).toBe(Number.MIN_SAFE_INTEGER);
        arrayWithMin.removeLastAdded();
        arrayWithMin.removeLastAdded();
        expect(arrayWithMin.getMin()).toBe(Number.MAX_SAFE_INTEGER);
    });

    test('should handle complex min value changes', () => {
        arrayWithMin.add(5);
        arrayWithMin.add(3);
        arrayWithMin.add(7);
        arrayWithMin.add(3);
        arrayWithMin.removeLastAdded();
        arrayWithMin.add(2);
        arrayWithMin.removeLastAdded();
        arrayWithMin.add(4);
        expect(arrayWithMin.array).toEqual([5, 3, 7, 4]);
        expect(arrayWithMin.minArray).toEqual([5, 3]);
        expect(arrayWithMin.getMin()).toBe(3);
    });
});
