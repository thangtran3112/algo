/**
 * Min Heap without the first element as array size
 * Time complexity: 0(log(n)) for insert, 0(log(n)) for extractMin, 0(1) for getMin
 * There could be implementation with array size as first element, but it's not used here
 */
export class MinHeap {
    private heap: number[];

    constructor(array: number[] = []) {
        this.heap = [...array];
        this.buildHeap();
    }

    private buildHeap(): void {
        // Start from last non-leaf node
        const startIdx = Math.floor(this.heap.length / 2) - 1;
        for (let i = startIdx; i >= 0; i--) {
            this.heapifyDown(i);
        }
    }

    /**
     * Left child index is 2 * i + 1, right child index is 2 * i + 2
     * Find the smallest child and swap with the parent
     * The parent node will be the smallest of the parent and both left and right children
     * Keep heapifying down either left or right child until the heap property is satisfied
     */
    private heapifyDown(i: number): void {
        let smallest = i;
        const leftChild = 2 * i + 1;
        const rightChild = 2 * i + 2;

        if (leftChild < this.heap.length && this.heap[leftChild] < this.heap[smallest]) {
            smallest = leftChild;
        }

        if (rightChild < this.heap.length && this.heap[rightChild] < this.heap[smallest]) {
            smallest = rightChild;
        }

        if (smallest !== i) {
            [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
            this.heapifyDown(smallest);
        }
    }

    /**
     * When inserting a new value, add it to the end of the heap and heapify up
     * Maintain the heap property by swapping with parent until the heap property is satisfied
     * Parent index is (i - 1) / 2
     * https://leetcode.com/explore/featured/card/heap/643/heap/4019/
     */
    insert(value: number): void {
        this.heap.push(value);
        this.heapifyUp(this.heap.length - 1);
    }

    private heapifyUp(i: number): void {
        if (i === 0) return;

        const parentIndex = Math.floor((i - 1) / 2);
        if (this.heap[parentIndex] > this.heap[i]) {
            [this.heap[parentIndex], this.heap[i]] = [this.heap[i], this.heap[parentIndex]];
            this.heapifyUp(parentIndex);
        }
    }

    /**
     * When extracting the minimum value, swap the first element with the last element
     * Remove the last element and heapify down
     * Maintain the heap property by swapping with the smallest child until the heap property is satisfied
     * Left child index is 2 * i + 1, right child index is 2 * i + 2
     * https://leetcode.com/explore/featured/card/heap/643/heap/4020/
     */
    extractMin(): number | undefined {
        if (this.heap.length === 0) return undefined;
        if (this.heap.length === 1) return this.heap.pop();

        const min = this.heap[0];
        // Swap the first element with the last element, and remove the last element
        this.heap[0] = this.heap.pop()!;
        this.heapifyDown(0);

        return min;
    }

    getMin(): number | undefined {
        return this.heap[0];
    }

    size(): number {
        return this.heap.length;
    }

    isEmpty(): boolean {
        return this.heap.length === 0;
    }

    getHeap(): number[] {
        return [...this.heap];
    }
}
