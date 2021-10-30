from heapq import heappop, heappush
from typing import List


class MaxNumberOfEnvetsAttended:
    # 1. Sort the events based on starting day of the event
    # 2. Now once you have this sorted events, every day check what are the events that can start today
    # 3. for all the events that can be started today, keep their ending time in heap.
    # - Wait why we only need ending times ?
    # i) from today onwards, we already know this event started in the past and all we need to know is when this event will finish
    # ii) Also, another key to this algorithm is being greedy, meaning I want to pick the event which is going to end the soonest.
    # - So how do we find the event which is going to end the soonest?
    # i) brute force way would be to look at all the event's ending time and find the minimum, this is probably ok for 1 day but as we can only attend 1 event a day,
    # we will end up repeating this for every day and that's why we can utilize heap(min heap to be precise) to solve the problem of finding the event with earliest ending time
    # 4. There is one more house cleaning step, the event whose ending time is in the past, we no longer can attend those event
    # 5. Last but very important step, Let's attend the event if any event to attend in the heap.

    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max(end for _, end in events)
        num_of_events_attended = 0
        event_id = 0
        min_heap = []

        # start one because events starts from one
        for day in range(1, total_days + 1):
            # add all events that end today
            while event_id < len(events) and events[event_id][0] == day:
                heappush(min_heap, events[event_id][1])
                event_id += 1

            # remove expired events
            while min_heap and min_heap[0] < day:
                heappop(min_heap)

            if min_heap:
                heappop(min_heap)
                num_of_events_attended += 1
        return num_of_events_attended
