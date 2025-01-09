import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = ""
        self._api_secret = ""
        self.url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        self.body_ = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        self._token = self._get_new_token()
        self.header = {
            "Authorization": f"Bearer {self._token}"
        }


    def search(self):
        testing_string = "TESTING"
        return testing_string

    def _get_new_token(self):
        self.response = requests.post(url=self.url, headers=self.header, data=self.body_)
        return self.response.json()["access_token"]

    def city_search(self, keyword):
        params = {
            "keyword": keyword,
            "include": "AIRPORTS"
        }
        search_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        city_info = requests.get(url=search_url, headers=self.header, params=params)
        return city_info.json()

    def flight_search(self, iatacode, departuredate, returndate, targetprice):
        search_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        params = {
            "originLocationCode": "MIA",
            "destinationLocationCode": iatacode,
            "departureDate": departuredate,
            "returnDate": returndate,
            "adults": 1,
            "currencyCode": "USD",
            "maxPrice": targetprice,
            "max": 3
        }

        print(params)
        flight_info = requests.get(url=search_url, headers=self.header, params=params)
        return flight_info.json()