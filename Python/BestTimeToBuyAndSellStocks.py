from typing import List


class BestTimeToBuyAndSellStocks:

    # Best time to buy and stocks ii
    #
    # On each day, you may decide to buy and/or sell the stock.
    # You can only hold at most one share of the stock at any time.
    # However, you can buy it then immediately sell it on the same day.
    #
    # THERE IS NO LIMIT ON THE NUMBER OF TRANSACTIONS !!!
    def maxProfit(self, prices):
        profit = 0
        i = 0
        while i < len(prices) - 1:
            # find valley
            while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
                i += 1
            valley = prices[i]
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
                i += 1
            profit += prices[i] - valley
        return profit

    # easier solution, and add positve diff together
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

     # Best time to buy and stocks iii
     #
     # Find the maximum profit you can achieve. You may complete at most two transactions.
     # You may not engage in multiple transactions at the same time,
     # (i.e. you must sell the stock before you buy again).
     #
     # this means there is NO OVERLAPPING transactions

    def maxProfit(self, prices: List[int]) -> int:
        t1_cost, t2_cost = inf, inf
        t1_profit, t2_profit = 0, 0

        for price in prices:
            t1_cost = min(t1_cost, price)
            t1_profit = max(t1_profit, price - t1_cost)

            t2_cost = min(t2_cost, price - t1_profit)
            t2_profit = max(t2_profit, price - t2_cost)

        return t2_profit

    # Best time to buy and stocks iv
    #
    # you can have k transactions
