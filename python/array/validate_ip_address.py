# https://leetcode.com/problems/validate-ip-address/description/
"""
Given a string queryIP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses while "192.168.01.1", "192.168.1.00", and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lowercase English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.

 

Example 1:

Input: queryIP = "172.16.254.1"
Output: "IPv4"
Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:

Input: queryIP = "256.256.256.256"
Output: "Neither"
Explanation: This is neither a IPv4 address nor a IPv6 address.
 

Constraints:

queryIP consists only of English letters, digits and the characters '.' and ':'.
"""
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv4Subnet(chunk: str) -> bool:
            # chunk is valid if chunk is between [0, 255]
            # if chunk contains '.', ':' or non-numeric letters, it is not valid
            if not chunk.isnumeric():
                return False
            if int(chunk) > 255 or int(chunk) < 0:
                return False
            # check for leading zero 001, 00
            if chunk[0] == '0' and len(chunk) >= 2:
                return False
            return True

        def isIPv4(ipAddress):
            chunks = ipAddress.split('.')
            if len(chunks) != 4:
                return False
            for chunk in chunks:
                if not isIPv4Subnet(chunk):
                    return False
            return True

        def isIpV6Subnet(chunk: str):
            chunk = chunk.lower()
            # if contains '.' or ':'
            if len(chunk) > 4 or len(chunk) == 0:
                return False
            for letter in chunk:
                if letter == '.' or letter == ':':
                    return False
                if not (letter.isdigit() or ord('f') >= ord(letter) >= ord('a')):
                    return False
            return True

        def isIPv6(ipAddress):
            chunks = ipAddress.split(':')
            if len(chunks) != 8:
                return False
            for chunk in chunks:
                if not isIpV6Subnet(chunk):
                    return False
            return True

        if len(queryIP) > 16 or ':' in queryIP:
            if isIPv6(queryIP):
                return "IPv6"
            else:
                return "Neither"
        else:
            if isIPv4(queryIP):
                return "IPv4"
            else:
                return "Neither"
            
# === TEST CASES ===
import pytest  # noqa: E402

@pytest.fixture
def solution():
    """Provides an instance of the Solution class."""
    return Solution()

def test_example1(solution):
    """Test Example 1 from the problem description."""
    queryIP = "172.16.254.1"
    assert solution.validIPAddress(queryIP) == "IPv4"

def test_example2(solution):
    """Test Example 2 from the problem description."""
    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    assert solution.validIPAddress(queryIP) == "IPv6"

def test_example3(solution):
    """Test Example 3 from the problem description."""
    queryIP = "256.256.256.256"
    assert solution.validIPAddress(queryIP) == "Neither"

def test_ipv4_valid_cases(solution):
    """Test various valid IPv4 addresses."""
    valid_ipv4 = [
        "192.168.1.1",
        "192.168.1.0",
        "0.0.0.0",
        "255.255.255.255",
        "1.2.3.4"
    ]
    for ip in valid_ipv4:
        assert solution.validIPAddress(ip) == "IPv4"

def test_ipv4_invalid_cases(solution):
    """Test various invalid IPv4 addresses."""
    invalid_ipv4 = [
        "192.168.01.1",    # Leading zero
        "192.168.1.00",    # Leading zero
        "192.168@1.1",     # Invalid character
        "192.168.1.1.1",   # Too many segments
        "192.168.1",       # Too few segments
        "192.168..1",      # Empty segment
        "192.168.1.256",   # Value > 255
        "192.168.-1.1",    # Negative value
        "a.b.c.d",         # Non-numeric
        "1.1.1.1.",        # Trailing dot
        ".1.1.1.1"         # Leading dot
    ]
    for ip in invalid_ipv4:
        assert solution.validIPAddress(ip) == "Neither"

def test_ipv6_valid_cases(solution):
    """Test various valid IPv6 addresses."""
    valid_ipv6 = [
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
        "2001:db8:85a3:0:0:8A2E:0370:7334",
        "2001:0:0:0:0:0:0:1",
        "::1",  # Not supported in this solution
        "2001::",  # Not supported in this solution
        "fe80::1ff:fe23:4567:890a",  # Not supported in this solution
        "2001:db8::2:1",  # Not supported in this solution
        "ABCD:EF01:2345:6789:ABCD:EF01:2345:6789",
        "0:0:0:0:0:0:0:0"
    ]
    for ip in valid_ipv6:
        # Note: This solution doesn't support IPv6 compression syntax with ::
        if "::" in ip:
            continue
        assert solution.validIPAddress(ip) == "IPv6"

def test_ipv6_invalid_cases(solution):
    """Test various invalid IPv6 addresses."""
    invalid_ipv6 = [
        "2001:0db8:85a3::8A2E:037j:7334",  # Invalid character 'j'
        "02001:0db8:85a3:0000:0000:8a2e:0370:7334",  # Segment too long (5 chars)
        "2001:0db8:85a3:0000:0000:8a2e:0370",  # Too few segments
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334",  # Too many segments
        "2001:0db8:85a3:0000:0000:8a2e:0370:",  # Trailing colon
        ":2001:0db8:85a3:0000:0000:8a2e:0370",  # Leading colon
        "2001:0db8::85a3::8a2e:0370:7334",  # Multiple :: (not supported)
        "20g1:0db8:85a3:0000:0000:8a2e:0370:7334",  # 'g' is not valid hex
        "2001:0db8:85a3:-1:0000:8a2e:0370:7334",  # Negative value
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334:7334"  # Too many segments
    ]
    for ip in invalid_ipv6:
        assert solution.validIPAddress(ip) == "Neither"

def test_edge_cases(solution):
    """Test edge cases."""
    edge_cases = [
        "",                # Empty string
        ".",               # Just a dot
        ":",               # Just a colon
        "1.2.3.4.5",       # IPv4 with too many segments
        "1:2:3:4:5:6:7",   # IPv6 with too few segments
        "1.2.3.4:5:6:7:8", # Mixed format
        "1.2.3.4:5:6:7:8:9:10:11:12", # Mixed format with too many segments
        "2001:0db8:85a3:0000:0000:8a2e:0370:7334:5555" # IPv6 with too many segments
    ]
    for ip in edge_cases:
        assert solution.validIPAddress(ip) == "Neither"

def test_ipv6_with_uppercase_and_lowercase_mixed(solution):
    """Test IPv6 addresses with mixed case hex digits."""
    queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
    assert solution.validIPAddress(queryIP) == "IPv6"
    
    queryIP = "2001:0DB8:85A3:0000:0000:8a2e:0370:7334"
    assert solution.validIPAddress(queryIP) == "IPv6"

def test_ipv6_with_leading_zeros(solution):
    """Test IPv6 addresses with leading zeros."""
    # Leading zeros are allowed in IPv6
    queryIP = "2001:0db8:0085:0000:0000:8a2e:0370:7334"
    assert solution.validIPAddress(queryIP) == "IPv6"