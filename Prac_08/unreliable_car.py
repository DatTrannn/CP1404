from car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        """Initialise a Car instance.
            reliability: a float between 0 and 100,
            that represents the percentage chance that the drive method will actually drive the car
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_number = random.randint(1, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
