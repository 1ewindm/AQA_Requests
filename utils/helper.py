import json

class Helper:
    def attach_response(self, response):
        response = json.dump(response, indent=4)