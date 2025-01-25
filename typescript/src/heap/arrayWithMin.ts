export class ArrayWithMin {
    array: number[];
    minArray: number[];

    constructor() {
        this.array = [];
        this.minArray = [];
    }

    add(value: number) {
        // when adding a new value, check if it is less than the current min
        // make sure to use <= to handle the case where the same value is added multiple times
        if (this.minArray.length === 0 || value <= this.minArray[this.minArray.length - 1]) {
            this.minArray.push(value);
        }
        this.array.push(value);
    }

    getMin(): number | undefined {
        return this.minArray[this.minArray.length - 1];
    }

    removeLastAdded() {
        if (this.array.length === 0) {
            return;
        }
        const lastAdded = this.array.pop();
        if (lastAdded === this.minArray[this.minArray.length - 1]) {
            this.minArray.pop();
        }
    }
}
