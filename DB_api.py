# -*- coding: utf-8 -*-
#working for Python 2.7.17
"""
Comment: API for interaction with the Deutsch Bahn REST APIs
Special: You HAVE TO subscribe to the chosen "sub-APIs" for all methods to work
"""
__author__ = "Janik Klauenberg"
__credits__ = "github.com/miltann"

__version__ = "0.1.5"
__maintainer__ = "Janik Klauenberg"
__email__ = "support@klauenberg.eu"
__status__ = "Mostly Working"
import requests
import json
import datetime

#Base URL and Authorization link
Base_url = "https://api.deutschebahn.com"
auth_link = "Authorization: Bearer  "

#API url for Fahrplan_api
Fahrplan_api = Base_url + "/fahrplan-plus/v1"

#API url for Betriebsstellen API
Betriebsstellen = Base_url + "/betriebsstellen/v1"

#API url for Station_data API
Station_data = Base_url + "/stada/v2"

#API url for BahnhofsFotos API
BahnhofsFotos = Base_url + "/bahnhofsfotos/v1"

#API url for Bahn

class API():
    """
    Comment: API Class, for the Deutsch Bahn REST APIs
    Input: Nothing, it's a class
    Output: As Input
    Special: Nothing
    """
    def __init__(self, token):
        """
        Comment: Standard Init method
        Input: API secret-token
        Output: nothing because this is the init
        Special: You have to subscribe to the servives you want to use with this Programm
        """
        global auth_link
        self.auth_token= auth_link + token
    def get_photographs(self, country):
        """
        Comment: Gets all photos for one country
        Input: Instancename and countrycode of the desired country
        Output: All photos for this country in json format
        Special: You have to be subcribed to the BahnhofsFotos API in the DB developer website
        """
        global BahnhofsFotos
        request_link = "/{}/stations"
        link = BahnhofsFotos + request_link.format(country)
        r = requests.get(link, headers={"Authorization" : self.auth_token, "Accept" : "application/json"})
        data = json.loads(r.content)
        return data
    def get_photographers(self):
        """
        Comment: Returns all Photographers and the data for them
        Input: Only name of the instance
        Output: All Photographers and their stats
        Special: Currently the only stats returned is the photographs count
        """
        global BahnhofsFotos
        request_link = "/photographers"
        link = BahnhofsFotos + request_link
        r = requests.get(link, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data
    def get_country_photographers(self, country):
        """
        Comment: Gets all Photographers of a country
        Input: Name of instance and countrycode
        Output: All Photographers for one country in json Format
        Special: similar to get_photographers(), but specific for one country
        """
        global BahnhofsFotos
        request_link = "/{}/photographers"
        link = BahnhofsFotos + request_link.format(country)
        r = requests.get(link, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data
    def get_photograph_country_stats(self, country):
        """
        Comment: Gets all stats for a specific country
        Input: Name of instance and countrycode of the desired country
        Output: Stats for country in json format
        Special: similar to get_stats() but specific for one country
        """
        global BahnhofsFotos
        request_link = "/{}/stats"
        link = BahnhofsFotos + request_link.format(country)
        r = requests.get(link, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data
    def get_photograph_stats(self):
        """
        Comment: Returns totals Stats for the BahnhofsFotos API
        Input: Only name of the instance
        Output: Stats for the whole BahnhofsFotos API in json format
        Special: similar to get_photograph_stats() but with stats for whole API
        """
        global BahnhofsFotos
        request_link = "/stats"
        link = BahnhofsFotos + request_link
        r = requests.get(link, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data
    def get_photograph_countries(self):
        """
        Comment: Returns Countries with specific Details to those countries
        Input: Only Name of instance
        Output: Details for all Countries in json format
        Special: Countrycodes can be taken from this function
        """
        global BahnhofsFotos
        request_link = "/countries"
        link = BahnhofsFotos + request_link
        r = requests.get(link, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data
    def get_betriebsstellen(self, query_string):
        """
        Comment: Returns all Stations of the Deutsche Bahn which match a query string
        Input: instance name, query_string is the stations name you are searching for
        Output: All matching results to the query string given
        Special: Nothing Special
        """
        global Betriebsstellen
        request_link = "/betriebsstellen"
        link = Betriebsstellen + request_link
        r = requests.get(link, headers={"Authorization" : self.auth_token}, params={"name" : query_string})
        data = json.loads(r.content)
        return data
    def get_betriebsstelle_abbrev(self, abbreveation):
        """
        Comment: Returns all Information for one specific Station by the given abbrevieation or the name
        Input: Name of instance, abbreveation is name or abbreveation of the station
        Output: All Information regarding a station
        Special: You have to be subscribed to this API for this to work
        """
        global Betriebsstellen
        request_link = "/betriebsstellen/{}"
        link = Betriebsstellen + request_link.format(abbreveation)
        r = requests.get(link, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data
    def get_station_data(self, query_string=None, limit=10000, federal_state=None):
        """
        Comment: Get all data for a station
        Input: Nothing required, optional: query_string is the exact name of the searched station, limit is the max output the APIs maximum is 10000, federal_staten filters only stations in the given federal state
        Output: Json object with result from REST api
        Special:
        """
        global Station_data
        request_link = "/stations"
        link = Station_data + request_link
        r = requests.get(link, headers={"Authorization" :self.auth_token}, params={"limit" : limit, "searchstring" : query_string, "federalstate" : federal_state})
        data = json.loads(r.content)
        return data
    def get_location(self, query_string):
        # To use this function you must subscribe to https://api.deutschebahn.com/fahrplan-plus/v1
        """
        Comment: get location details by searching for query_string
        Input: query_string is a search string
        Output: all matching results, but not only concrete results
        Special: Will return all similar query results
        """
        global Fahrplan_api
        global auth_token
        request_link = "/location/{}"
        link = Fahrplan_api + request_link.format(query_string)
        r = requests.get(link, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data

    def get_arrivals(self, id, date=None):
        # To use this function you must subscribe to https://api.deutschebahn.com/fahrplan-plus/v1
        """
        Comment: gets the arrivalBoard from a Trainstation at a given time
        Input: id from get_location, optional: date in the format yyyy-mm-ddThh:mm:ss
        Output: all arrivals in the given time
        Special: Nothing special
        """
        global Fahrplan_api
        global auth_token
        if date==None:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            date = str(today) + "T" + str(time)
        request_link = "/arrivalBoard/{}"
        link = Fahrplan_api + request_link.format(id)
        r = requests.get(link, params={"date" : date}, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data

    def get_departures(self, id, date=None):
        # To use this function you must subscribe to https://api.deutschebahn.com/fahrplan-plus/v1
        """
        Comment: Gets all departuers from a station
        Input: id from get_location, optional a date in format: yyyy-mm-ddThh:MM:ss
        Output: all departures after the given time
        Special: needs id from get_location
        """
        global Fahrplan_api
        if date==None:
            today = datetime.datetime.now().strftime("%Y-%m-%d")
            time = datetime.datetime.now().strftime("%H:%M:%S")
            date = str(today) + "T" + str(time)
        request_link = "/departureBoard/{}"
        link = Fahrplan_api + request_link.format(id)
        r = requests.get(link, params={"date":date}, headers={"Authorization" : self.auth_token})
        data = json.loads(r.content)
        return data

    def get_journey(self, id):
        # To use this function you must subscribe to https://api.deutschebahn.com/fahrplan-plus/v1
        """
        Comment: Currently not Working
        Input: detailsId from get_departures or get_arrivals
        Output: details about a train
        Special: Currently nor working
        """
        global Fahrplan_api
        request_link = "/journeyDetails/{}"
        link = Fahrplan_api + request_link.format(id).replace('%', '%25') # replace % as %25 because of percent encoding
        r = requests.get(link, headers={"Authorization" : self.auth_token})
        #data = json.loads(r.content)
        return r.content
