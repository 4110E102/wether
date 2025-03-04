import requests
def get_weather():
    url="https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-808BBF2F-7CD6-4EF3-95FF-847800F829C8"
    
    response = requests.get(url)
    result = response.json()["records"]["location"]
    
    return result