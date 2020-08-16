"""
A module to handle requests to the MUBI API
"""
import datetime
import logging
import json

import requests
from dateutil.parser import parse

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

BASE_URL = 'https://mubi.com/showing'


class MubiUtil:
    """A class that handles calls to the Mubi api"""

    def _fetch_raw_film_listings(self):
        response = requests.get(BASE_URL).text
        response = response.split('</script><script nomodule="" src="/_next/',
                    2)[0].split('script id="__NEXT_DATA__" type="application/json">', 2)[1]
        data = json.loads(response)
        return data['props']['initialState']['filmProgramming']['filmProgrammingsByChannel']['0']

    def get_leaving(self):
        """ returns the film leaving mubi today based on current date"""

        return self._fetch_raw_film_listings()[-1]['film']
