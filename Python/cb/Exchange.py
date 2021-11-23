from typing import List
import heapq
import datetime
import time


class Order:
    def __init__(self, price) -> None:
        self.price = price
        self.created_at = datetime.datetime.now()

    def isExpired(self) -> bool:
        return datetime.datetime.now() - self.created_at > datetime.timedelta(seconds=2)

    def __lt__(self, other):
        return self.price < other.price

    def __repr__(self) -> str:
        return str(self.price)

    def __le__(self, other):
        currenPrice = abs(self.price)
        otherPrice = abs(other.price)
        return currenPrice <= otherPrice

    def __ge__(self, other):
        currenPrice = abs(self.price)
        otherPrice = abs(other.price)
        return currenPrice >= otherPrice


class Exchange:

    def __init__(self, current_bid: List[int], current_ask: List[int]) -> None:
        self.current_ask = list(map(lambda x: Order(x), current_ask))
        heapq.heapify(self.current_ask)  # min heap for ask
        self.current_bid = list(map(lambda x: Order(-x), current_bid))
        heapq.heapify(self.current_bid)  # max head for bid

        print(self.current_ask, self.current_bid)

    def buyOrder(self, bid):
        self.deleteOrderIfNecessary(self.current_bid)
        self.deleteOrderIfNecessary(self.current_ask)
        bidOrder = Order(-bid)
        if not self.current_ask:
            heapq.heappush(self.current_bid, bidOrder)
            print('no one is selling, submitted buy order', bidOrder)
            return

        if bidOrder >= self.current_ask[0]:
            execution_price = heapq.heappop(self.current_ask)
            print('buy order is filled', execution_price)
            return execution_price
        # insert the buy order into max heap
        print('buy order is submitted', bidOrder)
        heapq.heappush(self.current_bid, bidOrder)

    def deleteOrderIfNecessary(self, heap):
        while heap:
            if heap[0].isExpired():
                heapq.heappop(heap)
            else:
                break

    def sellOrder(self, ask):
        self.deleteOrderIfNecessary(self.current_bid)
        self.deleteOrderIfNecessary(self.current_ask)
        askOrder = Order(ask)
        if not self.current_bid:
            heapq.heappush(self.current_ask, askOrder)
            print('no one is buying, submitted sell order', askOrder)
            return

        if askOrder <= self.current_bid[0]:
            execution_price = heapq.heappop(self.current_bid)
            print('sell order is filled', execution_price)
            return execution_price
        print('sell order is submitted', askOrder)
        heapq.heappush(self.current_ask, askOrder)


if __name__ == '__main__':
    obj = Exchange([90, 97, 99, 99, 100, 100], [119, 115, 114, 110, 110, 109])
    # obj.sellOrder(150)
    # obj.buyOrder(120)
    # obj.sellOrder(99)

    time.sleep(4)
    obj.buyOrder(120)
