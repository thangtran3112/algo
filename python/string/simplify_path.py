# https://leetcode.com/problems/simplify-path/description/
"""
You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:

A single period '.' represents the current directory.
A double period '..' represents the previous/parent directory.
Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
The simplified canonical path should follow these rules:

The path must start with a single slash '/'.
Directories within the path must be separated by exactly one slash '/'.
The path must not end with a slash '/', unless it is the root directory.
The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
Return the simplified canonical path.

 

Example 1:

Input: path = "/home/"

Output: "/home"

Explanation:

The trailing slash should be removed.

Example 2:

Input: path = "/home//foo/"

Output: "/home/foo"

Explanation:

Multiple consecutive slashes are replaced by a single one.

Example 3:

Input: path = "/home/user/Documents/../Pictures"

Output: "/home/user/Pictures"

Explanation:

A double period ".." refers to the directory up a level (the parent directory).

Example 4:

Input: path = "/../"

Output: "/"

Explanation:

Going one level up from the root directory is not possible.

Example 5:

Input: path = "/.../a/../b/c/../d/./"

Output: "/.../b/d"

Explanation:

"..." is a valid name for a directory in this problem.

 

Constraints:

1 <= path.length <= 3000
path consists of English letters, digits, period '.', slash '/' or '_'.
path is a valid absolute Unix path.
"""
import pytest
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        result = []
        # navigate from begining to end
        for part in parts:
            if part == '' or part == '.':
                # empty string means '//'
                # '.' means current directory
                # the path won't change, ignore these 2
                continue
            if part == '..':
                # go up one level, remove the last directory
                if len(result) > 0:
                    result.pop()
            else:
                # all other cases, such as '...', 'abc' are valid directory
                result.append(part)

        # reconstruct the absolute path
        ans = "/" + "/".join(result)
        return ans

# TEST CASES

@pytest.fixture
def solution_instance():
    return Solution()

def test_example1(solution_instance):
    """Input: path = "/home/" -> Output: "/home"""
    path = "/home/"
    expected = "/home"
    assert solution_instance.simplifyPath(path) == expected

def test_example2(solution_instance):
    """Input: path = "/home//foo/" -> Output: "/home/foo"""
    path = "/home//foo/"
    expected = "/home/foo"
    assert solution_instance.simplifyPath(path) == expected

def test_example3(solution_instance):
    """Input: path = "/home/user/Documents/../Pictures" -> Output: "/home/user/Pictures"""
    path = "/home/user/Documents/../Pictures"
    expected = "/home/user/Pictures"
    assert solution_instance.simplifyPath(path) == expected

def test_example4(solution_instance):
    """Input: path = "/../" -> Output: "/"""
    path = "/../"
    expected = "/"
    assert solution_instance.simplifyPath(path) == expected

def test_example5(solution_instance):
    """Input: path = "/.../a/../b/c/../d/./" -> Output: "/.../b/d"""
    path = "/.../a/../b/c/../d/./"
    expected = "/.../b/d"
    assert solution_instance.simplifyPath(path) == expected

def test_current_directory_path(solution_instance):
    """Input: path = "/./././." -> Output: "/"""
    path = "/./././."
    expected = "/"
    assert solution_instance.simplifyPath(path) == expected

def test_multiple_parent_directories(solution_instance):
    """Input: path = "/a/b/c/../../d" -> Output: "/a/d"""
    path = "/a/b/c/../../d"
    expected = "/a/d"
    assert solution_instance.simplifyPath(path) == expected

def test_consecutive_slashes(solution_instance):
    """Input: path = "////a///b//c////" -> Output: "/a/b/c"""
    path = "////a///b//c////"
    expected = "/a/b/c"
    assert solution_instance.simplifyPath(path) == expected

def test_single_root_directory(solution_instance):
    """Input: path = "/" -> Output: "/"""
    path = "/"
    expected = "/"
    assert solution_instance.simplifyPath(path) == expected

def test_triple_period_as_directory(solution_instance):
    """Input: path = "/..." -> Output: "/..."""
    path = "/..."
    expected = "/..."
    assert solution_instance.simplifyPath(path) == expected

def test_parent_beyond_root(solution_instance):
    """Input: path = "/../../../" -> Output: "/"""
    path = "/../../../"
    expected = "/"
    assert solution_instance.simplifyPath(path) == expected

def test_complex_path(solution_instance):
    """Input: path = "/a/./b/../../c/" -> Output: "/c"""
    path = "/a/./b/../../c/"
    expected = "/c"
    assert solution_instance.simplifyPath(path) == expected

def test_special_characters(solution_instance):
    """Input: path = "/a_b/c_d/e_f" -> Output: "/a_b/c_d/e_f"""
    path = "/a_b/c_d/e_f"
    expected = "/a_b/c_d/e_f"
    assert solution_instance.simplifyPath(path) == expected

def test_numeric_directories(solution_instance):
    """Input: path = "/123/456/789" -> Output: "/123/456/789"""
    path = "/123/456/789"
    expected = "/123/456/789"
    assert solution_instance.simplifyPath(path) == expected

def test_mixed_characters(solution_instance):
    """Input: path = "/abc123/def456/ghi789" -> Output: "/abc123/def456/ghi789"""
    path = "/abc123/def456/ghi789"
    expected = "/abc123/def456/ghi789"
    assert solution_instance.simplifyPath(path) == expected

def test_double_period_at_beginning(solution_instance):
    """Input: path = "/..hidden/file" -> Output: "/..hidden/file"""
    path = "/..hidden/file"
    expected = "/..hidden/file"
    assert solution_instance.simplifyPath(path) == expected

# To run these tests:
# 1. Make sure pytest is installed: pip install pytest
# 2. Navigate to the directory containing the test file and the solution file.
# 3. Run pytest in the terminal: pytest