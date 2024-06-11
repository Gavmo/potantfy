from dataclasses import dataclass
from datetime import datetime


@dataclass()
class Spot:
    spotId: int
    # Import as a string and have a new property that returns a datetime object
    spotTime: str
    activator: str
    frequency: str
    mode: str
    reference: str
    spotter: str
    source: str
    comments: str
    name: str
    locationDesc: str

    def __lt__(self, other):
        """Sort on the timestamps."""
        return self.timestamp < other.timestamp

    def __eq__(self, other):
        """Use the provided unique key"""
        return self.spotId == other.spotId

    @property
    def timestamp(self):
        return datetime.strptime(self.spotTime, "%Y-%m-%dT%H:%M:%S")

    @property
    def program(self):
        """Return the first two characters as the program"""
        return self.locationDesc[:2]
