import { longestPalindrome } from '../../src/string/palindrome';

describe('Longest Palindromic Substring', () => {
    test('basic odd length palindrome', () => {
        const result = longestPalindrome('babad');
        expect(['bab', 'aba']).toContain(result);
    });

    test('basic even length palindrome', () => {
        expect(longestPalindrome('cbbd')).toBe('bb');
    });

    test('single character string', () => {
        expect(longestPalindrome('a')).toBe('a');
    });

    test('empty string', () => {
        expect(longestPalindrome('')).toBe('');
    });

    test('all same characters', () => {
        expect(longestPalindrome('aaaa')).toBe('aaaa');
    });

    test('palindrome at start', () => {
        expect(longestPalindrome('aacdefg')).toBe('aa');
    });

    test('palindrome at end', () => {
        expect(longestPalindrome('defgaa')).toBe('aa');
    });

    test('palindrome in middle', () => {
        expect(longestPalindrome('defaaefg')).toBe('aa');
    });

    test('long palindrome', () => {
        expect(
            longestPalindrome(
                'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendure'
            )
        ).toBe('ranynar');
    });

    test('multiple palindromes same length', () => {
        const result = longestPalindrome('aabbaa');
        expect(result.length).toBe(6);
        expect(result).toBe('aabbaa');
    });

    test('with special characters', () => {
        expect(longestPalindrome('a#a')).toBe('a#a');
    });

    test('with numbers', () => {
        expect(longestPalindrome('12321')).toBe('12321');
    });

    test('alternating characters', () => {
        expect(longestPalindrome('abababa')).toBe('abababa');
    });

    test('overlapping palindromes', () => {
        expect(longestPalindrome('aaaa')).toBe('aaaa');
    });

    test('two character string same chars', () => {
        expect(longestPalindrome('cc')).toBe('cc');
    });

    test('two character string different chars', () => {
        const result = longestPalindrome('ab');
        expect(['a', 'b']).toContain(result);
    });

    test('complex mixed string', () => {
        expect(longestPalindrome('A man, a plan, a canal: Panama')).toMatch(/[aA]/); // Should return single character as spaces and punctuation count
    });
});

describe('Edge Cases and Performance', () => {
    test('very long string of same character', () => {
        const longString = 'a'.repeat(1000);
        expect(longestPalindrome(longString)).toBe(longString);
    });

    test('very long string with no long palindromes', () => {
        const longString = 'abcd'.repeat(250);
        expect(longestPalindrome(longString).length).toBe(1);
    });

    test('performance test with large input', () => {
        const start = Date.now();
        const longString = 'a'.repeat(1000) + 'b' + 'a'.repeat(1000);
        longestPalindrome(longString);
        const end = Date.now();
        expect(end - start).toBeLessThan(1000); // Should complete in less than 1 second
    });
});
