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
        self.base_url = "https://api.thunk.us/"

    def create(self):
        """ method for creating a thunk"""
        pass

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
        """ method for checking the status of a given UID """
        pass

    def _post_query(self, url, data = {}):
        """ query method to do HTTP POST

            Parameters:
                url -> the url to POST to
                data -> header_data as a dict

            Returns:
                Parsed JSON data as dict
                or
                None on error
        """
        values = urllib.urlencode(data)
        request = urllib2.Request(url, values)
        try:
            response = urllib2.urlopen(request)
        except IOError:
            return None
        json_data = response.read()
        data = json.loads(json_data)
        return data

    def _get_query(self, url):
        """ query method to do HTTP GET """
        pass

if __name__ == '__main__':
    import doctest
    doctest.doctest()
