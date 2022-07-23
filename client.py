# Using @property decorator
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        # if value < -273.15:
        #     raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


if __name__ == "__main__":
    letter = "a"
    target = "target"
    
    human = Celsius(37)
    
    print(human.temperature)

    print(human.to_fahrenheit())

    coldest_thing = Celsius(-300)
    
    print(coldest_thing.temperature)
    
    coldest_thing.temperature += 250
    
    print(coldest_thing.temperature)

    # print(letter in target)