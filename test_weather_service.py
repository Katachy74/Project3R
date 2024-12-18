import unittest
from weather_service import get_location_key, get_weather_data, get_coordinates

class TestWeatherService(unittest.TestCase):

    def test_get_location_key(self):
        key = get_location_key("Moscow")
        self.assertIsNotNone(key)

    def test_get_weather_data(self):
        key = get_location_key("Moscow")
        weather_data = get_weather_data(key)
        self.assertIsNotNone(weather_data)

    def test_get_coordinates(self):
        coord = get_coordinates("Moscow")
        self.assertIsNotNone(coord)
        self.assertIsInstance(coord, tuple)
        self.assertEqual(len(coord), 2)

if __name__ == '__main__':
    unittest.main()