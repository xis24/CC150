class SellDiminishingValueBalls:
    def maxProfit(self, inv, orders):
        inv.sort(reverse=True)
        inv.append(0)
        ans, i, width = 0, 0, 0

        while orders > 0:
            width += 1
            sell = min(orders, width * (inv[i] - inv[i + 1]))
            whole, remainder = divmod(sell, width)
            ans += width * (whole * (inv[i] + inv[i] - (whole - 1))) // 2 \
                + remainder * (inv[i] - whole)
            orders -= sell
            i += 1
        return ans
