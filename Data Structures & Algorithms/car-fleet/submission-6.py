class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Initialize Stack
        cars = []

        for x, v in zip(position, speed):
            cars.append([x, v])
        cars = sorted(cars)

        # Two cars form a fleet if the car behind reaches the target in less than
        # or equal to the time of the car ahead.
        fleet = 1
        x, v = cars.pop()
        prevTime = (target-x)/v
        
        while cars:
            x, v = cars.pop()
            time = (target-x)/v
            if time > prevTime:
                fleet += 1
                prevTime = time


        return fleet