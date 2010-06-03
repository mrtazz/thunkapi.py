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
        self.poke_states = ["good", "bad", "iffy", "unknown"]

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

    def poke(self, uid, state, payload=None):
        """ poke a thunk with the given UID

            Parameters:
                uid -> uid of the thunk to poke
        """
        if state not in self.poke_states:
            raise PokeStateError(("Invalid poke state %s given" % state))
        url = self.base_url + uid + "/" + state
        values = {}
        if payload is not None:
            values["payload"] = payload

        return self._query(url, values)

    def check(self, uid):
        """ method for checking the status of a given UID

            Parameters:
                uid -> the UID to check for
        """
        if isinstance(uid, list):
            extension = ",".join(["%s" % (ids) for ids in uid])
        else:
            extension = uid
        url = self.base_url + extension
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

# Custom Exception Classes

class PokeStateError(Exception):
    """ exception to raise if wrong poke state was provided
    """
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return repr(self.arg)
