# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""

import requests

def fetch_metadata(url):
    url_api = f"https://opengraph.lewagon.com/?url={url}"
    response = requests.get(url_api)
    if response.status_code != 200:
        return ''
    data = response.json()
    return data["data"]
fetch_metadata('https://www.lewagon.com')

    # TODO: implement this function!

# To manually test, please uncomment the following lines and run `python opengraph.py`:
# import pprint
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fetch_metadata("https://www.lewagon.com"))
