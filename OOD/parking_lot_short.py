from abc import ABC, abstractclassmethod
from enum import Enum


class VehicleSize(Enum):
    Motorcycle, Compact, Large = 1, 2, 3


class Vehicle(ABC):

    def __init__(self, licensePlate, spotNeeded, vehicleSize) -> None:
        self.parkingSpots = []
        self.licensePlate = licensePlate
        self.spotNeeded = spotNeeded
        self.vehicleSize = vehicleSize

    def parkInSpot(self, spot):
        self.parkingSpots.append(spot)

    def clearSpot(self):
        for i in range(len(self.parkingSpots)):
            self.parkingSpots[i].removeVehicle()
        self.parkingSpots.clear()

    def getSpotNeeded(self):
        return self.spotNeeded

    @abstractclassmethod
    def canFitInSpot(self, spot):
        pass


class Bus(Vehicle):
    def __init__(self, licensePlate) -> None:
        super().__init__(licensePlate, 5, VehicleSize.Large)

    def canFitInSpot(self, spot):
        return spot.getSize() == self.vehicleSize


class Car(Vehicle):
    def __init__(self, licensePlate) -> None:
        super().__init__(licensePlate, 1, VehicleSize.Compact)

    def canFitInSpot(self, spot):
        return spot.getSize() == VehicleSize.Large or spot.getSize() == VehicleSize.Compact


class Motorcycle(Vehicle):
    def __init__(self, licensePlate) -> None:
        super().__init__(licensePlate, 1, VehicleSize.Motorcycle)

    def canFitInSpot(self, spot):
        pass


# represents a level in a parking garage
class Level:

    def __init__(self, floor, numberSpots) -> None:
        self.floor = floor
        self.spots = []
        largeSpots = numberSpots // 4
        bikeSpots = numberSpots // 4
        compactSpots = numberSpots - largeSpots - bikeSpots
        SPOTS_PER_ROW = 10
        for i in range(numberSpots):
            vehicleSize = VehicleSize.Motorcycle
            if i < largeSpots:
                vehicleSize = VehicleSize.Large
            elif i < largeSpots + compactSpots:
                vehicleSize = VehicleSize.Compact

            row = i // SPOTS_PER_ROW
            self.spots.append(ParkingSpot(row, i, vehicleSize))
        self.availableSpots = numberSpots

    def availableSpots(self):
        return self.availableSpots

    # find a place to park this vehicle. return false if failed
    def parkVehicle(self, vehicle: Vehicle):
        if self.availableSpots() < vehicle.getSpotNeeded():
            return False
        spotNumber = self.findAvailableSpots(vehicle)
        if spotNumber < 0:
            return False

        return self._parkStartingAtSpot(spotNumber, vehicle)

    # find a spot to park this vehicle. Return the index of spot, -1 on failure
    def findAvailableSpots(self, vehicle: Vehicle):
        spotNeeded = vehicle.getSpotNeeded()
        lastRow = -1
        spotsFound = 0
        for i in range(len(self.spots)):
            if lastRow != self.spots[i].getRow():
                spotsFound = 0
                lastRow = self.spots[i].getRow()
            if self.spot[i].canFitVehicle(vehicle):
                spotsFound += 1
            else:
                spotsFound = 0
            if spotsFound == spotNeeded:
                return i - (spotNeeded - 1)
        return -1

    # parking a vehicle starting at the spot  SpotNumber, and continuing until vehicle.spotNeeded

    def _parkStartingAtSpot(self, spotNumber, vehicle: Vehicle):
        vehicle.clearSpot()
        success = True
        for i in range(spotNumber, spotNumber + vehicle.spotNeeded):
            success &= self.spots[i].park(vehicle)
        self.availableSpots -= vehicle.spotNeeded
        return success

    def spotFreed(self):
        self.availableSpots += 1


class ParkingLot:

    def __init__(self) -> None:
        self.levels = []
        NUM_LEVELS = 5
        for i in range(NUM_LEVELS):
            self.levels.append(Level(i, 30))

    def parkVehicle(self, vehicle):
        for i in range(len(self.levels)):
            if self.levels[i].parkVehicle(vehicle):
                return True
        return False


class ParkingSpot:
    def __init__(self, level, row, spotNumber, vehicleSize) -> None:
        self.level = level
        self.row = row
        self.spotNumber = spotNumber
        self.vehicleSize = vehicleSize
        self.vehicle = None

    def getSize(self):
        return self.vehicleSize

    def getRow(self):
        return self.row

    def canFitVehicle(self, vehicle):
        return not self.vehicle and vehicle.canFitInSpot(self)

    def park(self, vehicle):
        if not self.canFitVehicle(vehicle):
            return False
        self.vehicle = vehicle
        vehicle.park(self)
        return True

    def removeVehicle(self):
        self.level.spotFreed()
        self.vehicle = None
