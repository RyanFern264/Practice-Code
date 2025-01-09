import requests
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.request = requests.get(url="")
        #pprint(self.request.json())

    def update(self, line_id, data_inputs):
        self.push = requests.put(url=f"", json=data_inputs)
        self.push.raise_for_status()