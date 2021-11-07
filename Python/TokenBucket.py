import time
import threading


class TokenBucket:

    def __init__(self, maxBucketSize, refillRate) -> None:
        self.maxBucketSize = maxBucketSize
        self.refillRate = refillRate
        self.currentBucketSize = maxBucketSize
        self.lastRefillTimestamp = time.time_ns()
        self.lock = threading.Lock()

    def allowRequest(self, tokens: int) -> bool:
        self.lock.acquire()
        self.refill()

        if self.currentBucketSize > tokens:
            self.currentBucketSize -= tokens
            self.lock.release()
            return True
        self.lock.release()
        return False

    def refill(self):
        now = time.time_ns()
        tokenToAdd = (now - self.lastRefillTimestamp) * self.refillRate // 1e9
        self.currentBucketSize = min(
            self.currentBucketSize + tokenToAdd, self.maxBucketSize)
        self.lastRefillTimestamp = now
