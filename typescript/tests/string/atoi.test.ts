import { myAtoi } from '../../src/string/atoi';

describe('String to Integer (atoi)', () => {
    test('basic positive number', () => {
        expect(myAtoi('42')).toBe(42);
    });

    test('negative number with spaces', () => {
        expect(myAtoi('   -42')).toBe(-42);
    });

    test('number with words', () => {
        expect(myAtoi('4193 with words')).toBe(4193);
    });

    test('words before number', () => {
        expect(myAtoi('words and 987')).toBe(0);
    });

    test('number exceeding MAX_INT', () => {
        expect(myAtoi('2147483648')).toBe(2147483647);
    });

    test('number below MIN_INT', () => {
        expect(myAtoi('-2147483649')).toBe(-2147483648);
    });

    test('empty string', () => {
        expect(myAtoi('')).toBe(0);
    });

    test('only spaces', () => {
        expect(myAtoi('     ')).toBe(0);
    });

    test('plus sign', () => {
        expect(myAtoi('+1')).toBe(1);
    });

    test('leading zeros', () => {
        expect(myAtoi('000123')).toBe(123);
    });

    test('decimal number', () => {
        expect(myAtoi('3.14159')).toBe(3);
    });

    test('negative zero', () => {
        expect(myAtoi('-0')).toBe(0);
    });

    test('plus sign with spaces', () => {
        expect(myAtoi('    +11')).toBe(11);
    });

    test('invalid sign placement', () => {
        expect(myAtoi('+-12')).toBe(0);
    });

    test('multiple signs', () => {
        expect(myAtoi('++12')).toBe(0);
    });

    test('zero with spaces', () => {
        expect(myAtoi('   0000')).toBe(0);
    });

    test('number followed by sign', () => {
        expect(myAtoi('0-1')).toBe(0);
    });

    test('large number with spaces', () => {
        expect(myAtoi('  9999999999999')).toBe(2147483647);
    });

    test('negative large number', () => {
        expect(myAtoi('-9999999999999')).toBe(-2147483648);
    });
});
