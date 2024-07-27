from unittest.mock import Mock

# json = Mock()

# json.loads('{"key": "value"}')

# json.loads.assert_called()
# json.loads.assert_called_once()
# json.loads.assert_called_with('{"key": "value"}')
# json.loads.assert_called_once_with('{"key": "value"}')

# json.loads('{"key": "value"}')

# # json.loads.assert_called_once()

# json.loads(s='{"key": "value"}')

# json.loads.assert_called_with(s='{"key": "value"}')

# json = Mock()

# json.loads('{"key": "value"}')

# # print(json.loads.call_args_list)
# print(json.method_calls)

# from datetime import datetime



# wednesday = datetime(year=2025, month=1, day=1)
# sunday = datetime(year=2025, month=1, day=5)


# datetime = Mock()
# def is_weekday():
#     today = datetime.today()
#     return (0 <= today.weekday() < 5)

# datetime.today.return_value = wednesday

# assert is_weekday()

# datetime.today.return_value = sunday
# assert not is_weekday()


# side_effect

# import requests
# import unittest
# from requests.exceptions import Timeout
# from unittest.mock import Mock

# requests = Mock()

# def get_holidays():
#     r = requests.get("http:localhost/api/holidays")
#     if r.status_code == 200:
#         return r.json()
#     return None

# class TestHolidays(unittest.TestCase):
#     def test_get_holidays_timeout(self):
#         requests.get.side_effect = Timeout
#         with self.assertRaises(Timeout):
#             get_holidays()

# if __name__ == "__main__":
#     unittest.main()

import requests
import unittest
from unittest.mock import Mock

requests = Mock()

def get_holiday():
    r = requests.get("https://localhost/api/holidays")
    if r.status_code == 200:
        return r.json()
    return None

class TestHolidays(unittest.TestCase):
    def log_request(self, url):
        print(f"Making a request to {url}.")
        print("Request recieved!")

        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            "12/25": "christmas",
            "7/4": "Independence Day"
        }