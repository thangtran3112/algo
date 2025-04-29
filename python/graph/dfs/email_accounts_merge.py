# https://leetcode.com/problems/accounts-merge/description/
"""
Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

 

Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
"""

from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self):
        self.root = {}
        self.rank = defaultdict(int)

    # Path compression, to make consitant find by directly connecting to root
    def find(self, x):
        if x not in self.root:
            self.root[x] = x
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    # union by rank, to balance the depth, between 2 disjoint sets
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            # already connected
            return
        if self.rank[root_x] > self.rank[root_y]:
            self.root[root_y] = root_x
        elif self.rank[root_y] > self.rank[root_x]:
            self.root[root_x] = root_y
        else:
            # both sets have equal depth, we need to increment rank of new root 
            self.root[root_y] = root_x
            self.rank[root_x] += 1

class SolutionUnionFind:
    # merge by email. But we can also merge by account index
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        uf = UnionFind()
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                uf.union(first_email, email)
                email_to_name[email] = name

        # Group email by its corresponding root in UnionFind
        root_to_emails = defaultdict(list)
        for email in email_to_name:
            root = uf.find(email)
            root_to_emails[root].append(email)

        # format the result
        result = []
        for root, emails_list in root_to_emails.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails_list))

        return result
    
class SolutionDFS:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {}
        graph = defaultdict(list)

        # Step 1: Build the graph
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for email in emails:
                email_to_name[email] = name
                graph[emails[0]].append(email)
                graph[email].append(emails[0])

        # Step 2: DFS to find connected components
        visited = set()
        result = []

        def dfs(email, collected):
            visited.add(email)
            collected.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, collected)

        for email in email_to_name:
            if email not in visited:
                collected = []
                dfs(email, collected)
                result.append([email_to_name[email]] + sorted(collected))

        return result
    
# === TEST CASES ===
import pytest
from typing import List
from collections import defaultdict

@pytest.fixture(params=[SolutionUnionFind, SolutionDFS],
               ids=["UnionFind", "DFS"])
def solution_instance(request):
    """Fixture to provide instances of both solution classes."""
    return request.param()

def normalize_result(result: List[List[str]]) -> List[List[str]]:
    """
    Sort accounts for consistent comparison, since order doesn't matter.
    Each account's emails are already sorted.
    """
    return sorted(result, key=lambda x: (x[0], x[1] if len(x) > 1 else ""))

def test_example1(solution_instance):
    """Test Example 1 from the problem description."""
    accounts = [
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["Mary", "mary@mail.com"],
        ["John", "johnnybravo@mail.com"]
    ]
    expected = [
        ["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["Mary", "mary@mail.com"]
    ]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_example2(solution_instance):
    """Test Example 2 from the problem description."""
    accounts = [
        ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
        ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
        ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
        ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
        ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]
    ]
    expected = [
        ["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
        ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"],
        ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
        ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
        ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"]
    ]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_single_account(solution_instance):
    """Test with a single account."""
    accounts = [["Alex", "alex@example.com", "alex@gmail.com"]]
    expected = [["Alex", "alex@example.com", "alex@gmail.com"]]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_complex_merge(solution_instance):
    """Test with a more complex merge scenario involving multiple connections."""
    accounts = [
        ["David", "d1@mail.com", "d2@mail.com"],
        ["David", "d3@mail.com", "d4@mail.com"],
        ["David", "d2@mail.com", "d3@mail.com"],
        ["David", "d5@mail.com"]
    ]
    expected = [
        ["David", "d1@mail.com", "d2@mail.com", "d3@mail.com", "d4@mail.com"],
        ["David", "d5@mail.com"]
    ]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_multiple_names_same_email(solution_instance):
    """Test with different names having the same email (not allowed per problem constraint)."""
    accounts = [
        ["John", "john@example.com"],
        ["Jane", "john@example.com"]
    ]
    # The assumption is the emails define the person, so these should merge under one name
    # Per the problem statement: "A person can have any number of accounts initially,
    # but all of their accounts definitely have the same name."
    # This is a edge case testing behavior that shouldn't happen per constraints
    result = solution_instance.accountsMerge(accounts)
    # The result will depend on which name gets picked first, but should have only one account
    assert len(result) == 1
    assert len(result[0]) == 2  # Name + 1 email
    assert result[0][1] == "john@example.com"

def test_all_accounts_separate(solution_instance):
    """Test when all accounts are separate (no merging needed)."""
    accounts = [
        ["Alice", "alice@example.com"],
        ["Bob", "bob@example.com"],
        ["Charlie", "charlie@example.com"]
    ]
    expected = [
        ["Alice", "alice@example.com"],
        ["Bob", "bob@example.com"],
        ["Charlie", "charlie@example.com"]
    ]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_circular_connections(solution_instance):
    """Test with circular connections between accounts."""
    accounts = [
        ["Alex", "a@mail.com", "b@mail.com"],
        ["Alex", "b@mail.com", "c@mail.com"],
        ["Alex", "c@mail.com", "d@mail.com"],
        ["Alex", "d@mail.com", "a@mail.com"]
    ]
    expected = [["Alex", "a@mail.com", "b@mail.com", "c@mail.com", "d@mail.com"]]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_duplicate_emails_in_account(solution_instance):
    """Test with duplicate emails within the same account."""
    accounts = [["John", "john@example.com", "john@example.com"]]
    expected = [["John", "john@example.com"]]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_multiple_duplicates_across_accounts(solution_instance):
    """Test with multiple duplicate emails across different accounts."""
    accounts = [
        ["John", "a@mail.com", "b@mail.com"],
        ["John", "b@mail.com", "c@mail.com"],
        ["Mary", "d@mail.com"],
        ["John", "e@mail.com", "f@mail.com"],
        ["John", "f@mail.com", "g@mail.com"],
        ["John", "g@mail.com", "a@mail.com"]
    ]
    expected = [
        ["John", "a@mail.com", "b@mail.com", "c@mail.com", "e@mail.com", "f@mail.com", "g@mail.com"],
        ["Mary", "d@mail.com"]
    ]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_chained_connections(solution_instance):
    """Test with connections forming a chain that all need to merge."""
    accounts = [
        ["Alex", "a1@mail.com", "a2@mail.com"],
        ["Alex", "a2@mail.com", "a3@mail.com"],
        ["Alex", "a3@mail.com", "a4@mail.com"],
        ["Alex", "a4@mail.com", "a5@mail.com"]
    ]
    expected = [["Alex", "a1@mail.com", "a2@mail.com", "a3@mail.com", "a4@mail.com", "a5@mail.com"]]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)

def test_large_number_of_accounts(solution_instance):
    """Test with a large number of unrelated accounts."""
    accounts = [["User"+str(i), "user"+str(i)+"@mail.com"] for i in range(100)]
    expected = [["User"+str(i), "user"+str(i)+"@mail.com"] for i in range(100)]
    result = solution_instance.accountsMerge(accounts)
    assert normalize_result(result) == normalize_result(expected)