class HardcodedDb:
    def __init__(self):
        self._user_data = {
            "eddie123": {
                "device_id": "samsung123",
                "region": "Stockholm-väst"
            },
            "malin123": {
                "device_id": "iphone123",
                "region": "Uppsala"
            }
        }

        self._geography_data = {
            "Stockholm-väst": {
                "area": "list of geojson points forming a polygon of the geographic area"
            },
            "Uppsala": {
                "area": "list of geojson points forming a polygon of the geographic area"
            }
        }

    def get_device_id_for_user(self, user_id):
        if user_id not in self._user_data or "device_id" not in self._user_data[user_id]:
            return None

        return self._user_data[user_id]["device_id"]

    def get_user_ids_in_region(self, region_id):
        return [x for x in self._user_data if self._user_data[x]["region"] == region_id]

    def get_region_from_point(self, lat, long):
        print(lat, long)
        return "Uppsala"  # Do some magic to get region
