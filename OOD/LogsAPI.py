import time
from functools import reduce


class Log:
    def __init__(self, timestamp, action) -> None:
        self.timestamp = timestamp
        self.action = action
        self.cost = 1

    def __repr__(self) -> str:
        return str(self.timestamp) + " " + self.action


class LogsAPI:

    def __init__(self) -> None:
        self.logList = []

    def insertLog(self, log):
        self.logList.append(log)

    # log format: {timestamp, action}
    def mapping(self, func):
        return list(map(func, self.logList))

    def findAction(self, action):
        filtered = filter(lambda x: x.action == action, self.logList)
        return list(map(lambda x: x.timestamp, filtered))

    def countAction(self, action):
        filtered = filter(lambda x: x.action == action, self.logList)
        return len(filtered)


if __name__ == '__main__':
    obj = LogsAPI()
    obj.insertLog(Log(time.time(), "OFFER"))
    obj.insertLog(Log(time.time() + 1, "OFFER"))
    obj.insertLog(Log(time.time() + 2, "CONG"))
    obj.insertLog(Log(time.time() + 3, "CONG"))
    obj.insertLog(Log(time.time() + 4, "OFFER"))
    obj.insertLog(Log(time.time() + 4, "SOMETHING"))
    obj.insertLog(Log(time.time() + 2, "CONG"))

    print(obj.findAction("OFFER"))
    print(obj.countAction("OFFER"))
