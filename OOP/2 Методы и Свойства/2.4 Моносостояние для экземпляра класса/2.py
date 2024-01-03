class WeatherStation:
    __shared_attr = {"temperature": 0,
                     "humidity": 0,
                     "pressure": 0
                     }

    def __init__(self):
        self.__dict__ = WeatherStation.__shared_attr

    def update_data(self, temperature, humidity, pressure):
        self.__shared_attr['temperature'] = temperature
        self.__shared_attr['humidity'] = humidity
        self.__shared_attr['pressure'] = pressure


    def get_current_data(self):
        return self.__shared_attr['temperature'], self.__shared_attr['humidity'], self.__shared_attr['pressure']

sensor1 = WeatherStation()
assert sensor1.temperature == 0
assert sensor1.humidity == 0
assert sensor1.pressure == 0
sensor2 = WeatherStation()
assert sensor2.get_current_data() == (0, 0, 0)
sensor1.update_data(25, 60, 103)
assert sensor1.get_current_data() == (25, 60, 103)
assert sensor2.get_current_data() == (25, 60, 103)
sensor3 = WeatherStation()
assert sensor3.get_current_data() == (25, 60, 103)
sensor3.update_data(50, 20, 10)
assert sensor1.get_current_data() == (50, 20, 10)
assert sensor2.get_current_data() == (50, 20, 10)
print('Good')