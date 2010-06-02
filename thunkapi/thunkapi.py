# encoding: utf-8

""" library for the thunk.us API """

import urllib
import urllib2
import json

class Thunk:
    """ class for creating an object which can talk to the
        thunk.us API
    """
    def __init__(self):
        self.base_url = "http://thunk.us/"

    def create(self, name=None):
        """ method for creating a thunk

            Parameters:
                name -> optional name of the thunk
        """
        values = {}
        if name is not None:
            values["name"] = name
        data = self._query(self.base_url, values)
        return data

    def poke(self, uid):
        """ poke a thunk with the given UID

            Parameters:
                uid -> uid of the thunk to poke
        """
        pass

    def destroy(self, uid):
        """ method to destroy a thunk with the given UID """
        pass

    def check(self, uid):
        """ method for checking the status of a given UID

            Parameters:
                uid -> the UID to check for
        """
        url = self.base_url + uid
        return self._query(url)

    def _query(self, url, data = None):
        """ query method to do HTTP POST/GET

            Parameters:
                url -> the url to POST/GET
                data -> header_data as a dict (only for POST)

            Returns:
                Parsed JSON data as dict
                or
                None on error
        """
        if data is not None: # we have POST data if there is data
            values = urllib.urlencode(data)
            request = urllib2.Request(url, values)
        else: # do a GET otherwise
            request = urllib2.Request(url)
        try:
            response = urllib2.urlopen(request)
        except IOError: # no connection
            return None
        json_data = response.read()
        data = json.loads(json_data)
        return data

if __name__ == '__main__':
    import doctest
    doctest.doctest()
