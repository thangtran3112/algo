function buildCenterExpansion(s: string, left: number, right: number): string {
    while (left >= 0 && right < s.length && s[left] === s[right]) {
        left--;
        right++;
    }
    return s.slice(left + 1, right);
}

export function longestPalindrome(s: string): string {
    let longest = '';
    for (let i = 0; i < s.length; i++) {
        const odd = buildCenterExpansion(s, i, i);
        const even = buildCenterExpansion(s, i, i + 1);
        longest = longest.length > odd.length ? longest : odd;
        longest = longest.length > even.length ? longest : even;
    }
    return longest;
}
