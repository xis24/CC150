import collections
from enum import Enum


# Design a locker

# Use case
# 1. put a package into a locker
# 3. Find a locker space for a package and reserve it
# 4. Track if a package in a locker or not
# 2. get a package from a locker
# 5. Shipping Status?
# 6. Expiration for a package in a locker
# 7. Access control - normal user cannot do admin works ?
# 8. History ?
# 9. Multiple package in a slot ?


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    EXTRA_LARGE = 4


class Package:

    def __init__(self, packageID: int, packageSize: Size, zipCode: str) -> None:
        self.packageId = packageID
        self.packageSize = packageSize
        self.zipCode = zipCode


class Locker:

    def __init__(self, lockerID: int, zipCode: str, lockerSize: Size) -> None:
        self.lockerID = lockerID
        self.zipCode = zipCode
        self.lockerSize = lockerSize
        self.package = None  # initially there is no package

    def storePackage(self, package: Package) -> None:
        self.package = package

    def removePackage(self) -> None:
        # we might need mechanism to remove package
        self.package = None

    def isFitIn(self, package: Package) -> bool:
        return self.lockerSize == self.package.packageSize

    def hasPackage(self):
        return self.package


class LockerSystem:

    def __init__(self, xlargeLockerCount: int,
                 largeLockerCount: int,
                 midLockerCount: int,
                 smallLockerCount: int) -> None:
        # stores package id -> Locker
        self.occupiedLocker = {}
        self.lockerInvetory = {
            Size.EXTRA_LARGE: self._generateLocker(xlargeLockerCount, Size.EXTRA_LARGE),
            Size.LARGE: self._generateLocker(largeLockerCount, Size.LARGE),
            Size.MEDIUM: self._generateLocker(largeLockerCount, Size.MEDIUM),
            Size.SMALL: self._generateLocker(smallLockerCount, Size.SMALL)
        }

    def _generateLocker(self, count: int, size: Size):
        lockers = collections.deque([])
        for i in range(count):
            lockers.append(Locker(str(size) + i, '10001', size))
        return lockers

    def isLockerAvailable(self, package: Package) -> bool:
        return len(self.lockerInvetory[package.packageSize]) > 0

    def searchPackage(self, package: Package) -> Package:
        if package.packageId in self.occupiedLocker:
            return None
        return self.occupiedLocker[package.packageId]

    def removePackage(self, package: Package) -> Locker:
        if not package.packageId in self.occupiedLocker:
            return None
        occupiedLocker = self.occupiedLocker[package.packageId]
        occupiedLocker.removePackage()

        # increase inventory
        self.lockerInvetory[package.packageSize].append(occupiedLocker)

        return occupiedLocker

    def addPackage(self, package: Package):
        if not self.isLockerAvailable(package.packageSize):
            return False
        locker = self.lockerInvetory[package.packageSize].pop()
        locker.setPackage(package)
        self.occupiedLocker[package.packageId] = locker
        return True
