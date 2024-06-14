"""

"""
import json

try:
    from .spot import Spot
except ImportError:
    from spot import Spot


class Spots:
    def __init__(self):
        self.all_spots = []

    def add_spot(self, pota_spot_json_obj):
        """Take the pota spot object and put it in the spot data class"""
        new_spot_obj = Spot(
            pota_spot_json_obj["spotId"],
            pota_spot_json_obj["spotTime"],
            pota_spot_json_obj["activator"],
            pota_spot_json_obj["frequency"],
            pota_spot_json_obj["mode"],
            pota_spot_json_obj["reference"],
            pota_spot_json_obj["spotter"],
            pota_spot_json_obj["source"],
            pota_spot_json_obj["comments"],
            pota_spot_json_obj["name"],
            pota_spot_json_obj["locationDesc"],
        )
        self.all_spots.append(new_spot_obj)
        if not hasattr(self, f"{new_spot_obj.program}_spots"):
            setattr(self, f"{new_spot_obj.program}_spots", [])
        getattr(self, f"{new_spot_obj.program}_spots").append(new_spot_obj)

    def import_json(self, json_data):
        pota_spots = json.loads(json_data)
        for spot in pota_spots:
            if spot["spotId"] not in self.all_spots:
                self.add_spot(spot)

    def get_spots_by_program(self, program_cd):
        """Since the lists are dynamically generated, this function will return the specific program if it exists"""
        # Need an empty list to prevent iteration of a Nonetype
        return_list = []
        if hasattr(self, f"{program_cd.upper()}_spots"):
            return_list = getattr(self, f"{program_cd.upper()}_spots")
        return return_list

    def get_latest_unique_parks(self, program_cd=None):
        if program_cd:
            spot_dict = {}
            for spot in self.get_spots_by_program(program_cd):
                if spot.reference not in spot_dict.keys():
                    spot_dict[spot.reference] = []
                spot_dict[spot.reference].append(spot)
            # Now only leave the most recent spot in the dictionary
            for park in spot_dict.keys():
                spot_dict[park] = max(spot_dict[park])
            return spot_dict


# Quick tests
if __name__ == '__main__':
    with open("../tests/testjson", "r") as json_file:
        a = Spots()
        a.import_json(json_file.read())
        assert len(a.get_spots_by_program("au")) == 5
        b = a.get_latest_unique_parks("jp")
        pass
