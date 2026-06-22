"""
1672. Richest Customer Wealth

You are given an m x n integer grid accounts where accounts[i][j] is the
amount of money the ith customer has in the jth bank. Return the wealth
that the richest customer has. A customer's wealth is the sum of every
bank account they own.

Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6

Example 2:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10

Example 3:
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17
"""


def maximum_wealth(accounts) -> int:
    return max(sum(account) for account in accounts)


if __name__ == "__main__":
    print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))           # 6
    print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))         # 10
    print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))  # 17
