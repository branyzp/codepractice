# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

# This is the sliding window method using 2 pointers

def MaxProfit(prices):
    # set up two pointers, one for buy and one for sell
    buyPtr,sellPtr = 0,1
    # set up maxProfit count
    maxP = 0

    while sellPtr < len(prices):
        # if price at sell is higher than buy, calculate profit and check if profit is higher than maxProfit so far
        if prices[sellPtr] > prices[buyPtr]:
            profit = prices[sellPtr] - prices[buyPtr]
            maxP = max(maxP,profit)
        else:
            # if price at index sellPtr is less than buyPtr, switch buyPtr to the new low
            buyPtr=sellPtr
        # increment sellPtr to iterate through the list
        sellPtr+=1
    
    print(maxP)


prices = [7, 2, 6, 3, 1, 4]
MaxProfit(prices)
