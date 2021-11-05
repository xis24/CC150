# ElevatorDesign

## requirment

- An elevator can move up, down or standstill.
- An elevator can transfer passengers from one floor in a building to another floor in the minimum time possible.
- Elevator door can only open when it is standstill in a floor (i.e. not moving).
- Let's assume we have 200 floors, and 100 cars
- specs of each elevator

  - number of passsengers
  - max load
  - max speed of elevator can move

- what do we want to optimize?

  - min wait time the system ?
  - min wait time of individual passenger
  - max throughput
  - min power usage/cost

- do we have zones ?

  - operational zone
  - we can separate our elevator to different zones

  1. first approach

  - from 1-50 operaetored by 25 elevator
  - from 51 -100 operatator by 25 elevator
  - from 101-150 operatator by 25 elevator
  - from 151-200 operator by 25 elevator

  2. we can also separate to even/odd evelator, each zone could be a independent system

  - If we were use first appproach, the design problem becomes 50 floors and 25 evelators
  - If 2nd approach, the design is 100 floors and 50 elevators

  - additional

  1. emergy alarm
  2. vip or utility evelator

  Object:

  - passenger (not needed for this implementation)
  - elevator
  - floors
  - Doors
  - Button panels
  - Dispatcher (select elevator)
  - Elevator System
  - Montior System

  Use Cases:

  - move/stop the elevator
  - open/close doors
  - indicating moving
  - indicating elevator position
  - trigger emergency breaks
  - making emergency call

Interface and class

```python
class Button:
    def pressDown()
    def pressUp()

class ElevatorButton(Button):
    # inside of elevator


class HallButton(Button):
    # outside of each floor

class Door():
    # each floor has a door instance
    open()
    close()
    isOpen()

class ElevatorMotion:
    move(destination floor)
    stop()
```

## Algorithm

### First Come First Serve

- request goes into a queue

4 states

1. idle
2. moving same direciton towards passenger that passenger wants to go
3. moving same direciton toawrds passenger that ooposed direction passenger want to go
4. going away from the passenger

### Shortest seek time

1. priority queue / minheap

- startvation

### Scan (elevator algorithm)

- go all the up/down
- check if we should stop at each floor

cons: car are continously moving, high cost

### LOOK (look ahead)

- move based on the request
- there is no request, it will stop.

### destination dispatch

separate panel to enter floor

- no stop between.
- all people goes together
