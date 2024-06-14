"""
Ingest the spots
Send the spots to ntfy

"""
from datetime import datetime
import requests
import time

import config
from objects.SpotManager import Spots


def get_data():
    """The get_data function will facilitate testing.  When implementing with production data it will retrieve json from
    the API
    """
    return_data = ""
    spot_data = requests.get(config.spot_endpoint)
    if spot_data.status_code == 200:
        return_data = spot_data.text
    return return_data


def send_notification(spot):
    requests.post(f"{config.ntfy_host}/{config.ntfy_topic}",
                  data=f"{spot.activator} on {spot.frequency}({spot.mode}) at {spot.name}({spot.reference})".encode(encoding='utf-8'),
                  headers={
                      "Title": "Parks On The Air"
                  },
                  auth=(config.ntfy_user, config.ntfy_key))
    pass


def run(interval=5):
    """Interval is the refresh in minutes."""
    spots = Spots()
    run_time = datetime.now()
    processed_ids = []
    while True:
        spots.import_json(get_data())
        for park, spot in spots.get_latest_unique_parks("au").items():
            if spot.spotId not in processed_ids:
                send_notification(spot)
        processed_ids = [x.spotId for _, x in spots.get_latest_unique_parks("au").items()]
        time.sleep(interval * 60)
    pass


if __name__ == '__main__':
    run()
