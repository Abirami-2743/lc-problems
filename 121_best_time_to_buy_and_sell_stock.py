"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given
stock on the ith day. You want to maximize your profit by choosing a
single day to buy one stock and choosing a different day in the future
to sell that stock. Return the maximum profit you can achieve. If you
cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
"""


def max_profit(prices) -> int:
    min_price = float("inf")
    best = 0
    for price in prices:
        min_price = min(min_price, price)
        best = max(best, price - min_price)
    return best


if __name__ == "__main__":
    print(max_profit([7, 1, 5, 3, 6, 4]))  
    print(max_profit([7, 6, 4, 3, 1]))     
