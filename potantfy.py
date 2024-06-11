"""
Ingest the spots
Send the spots to ntfy

"""
from datetime import datetime

from objects.SpotManager import Spots


def get_data():
    """The get_data function will facilitate testing.  When implementing with production data it will retrieve json from
    the API
    """
    return_data = ""
    with open("tests/testjson", "r") as json_file:
        return_data = json_file.read()
    return return_data


def run(interval=5):
    """Interval is the refresh in minutes."""
    spots = Spots()
    run_time = datetime.now()
    spots.import_json(get_data())
    pass


if __name__ == '__main__':
    run()
