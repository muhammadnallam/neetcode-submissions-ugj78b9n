class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Initialize Stack
        cars = []

        for x, v in zip(position, speed):
            cars.append([x, v])
        cars = sorted(cars)

        fleet = 1
        x, v = cars.pop()
        prevTime = (target-x)/v
        
        # First car
        while cars:
            x, v = cars.pop()
            time = (target-x)/v
            if time > prevTime:
                fleet += 1
                prevTime = time

            print(f"Prev/Time = {prevTime}, {time}")


        return fleet