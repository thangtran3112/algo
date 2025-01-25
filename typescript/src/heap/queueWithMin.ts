/**
 * Keep track of the minimum value in a queue
 * Dequeue the first added element
 * Time complexity: 0(1) for getMin, 0(n) for add, 0(n) for removeFirstAdded
 */
export class QueueWithMin {
    array: number[];
    minArray: number[];

    constructor() {
        this.array = [];
        this.minArray = [];
    }

    add(value: number) {
        this.array.push(value);
        while (this.minArray.length > 0 && this.minArray[this.minArray.length - 1] > value) {
            this.minArray.pop();
        }
        this.minArray.push(value);
    }

    getMin(): number | undefined {
        if (this.minArray.length === 0) return undefined;
        return this.minArray[0];
    }

    removeFirstAdded() {
        if (this.array.length === 0) {
            return;
        }
        const firstValue = this.array.shift();
        if (firstValue === this.minArray[0]) {
            this.minArray.shift();
        }
        return firstValue;
    }
}
