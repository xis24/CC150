class CountAllValidPickupAndDeliveryOptions:

    '''
    Given n orders, each order consist in pickup and delivery services. 
    Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).  
    Since the answer may be too large, return it modulo 10^9 + 7.

    Input: n = 1
    Output: 1
    Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

    Input: n = 2
    Output: 6
    Explanation: All possible orders: 
    (P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
    This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.     

    '''

    def countOrders(self, n: int) -> int:
        ans = 1
        MOD = 10**9 + 7
        for i in range(2, n + 1):
            space_count = (i - 1) * 2 + 1
            ans *= space_count * (space_count + 1) // 2
            ans %= MOD
        return ans
