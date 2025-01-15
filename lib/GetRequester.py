import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status() 
            return response.content
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return None
        
    def load_json(self):
        try:
            response_body = self.get_response_body()
            if response_body is not None:
                return json.loads(response_body)
            return None
        except json.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            return None