# -*- coding: UTF-8 -*-
import json
import logging
import requests
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

LOG = logging.getLogger(__name__)

HEADERS = {"Content-type": "application/json"}
RESTAPI_37 = "https://grch37.rest.ensembl.org"
RESTAPI_38 = "https://rest.ensembl.org/"
PING_ENDPOINT = "info/ping"


class EnsemblRestApiClient:
    """A class handling requests and responses to and from the Ensembl REST APIs.
    Endpoints for human build 37: https://grch37.rest.ensembl.org
    Endpoints for human build 38: http://rest.ensembl.org/
    Documentation: https://github.com/Ensembl/ensembl-rest/wiki
    doi:10.1093/bioinformatics/btu613
    """

    def __init__(self, build="37"):
        if build == "38":
            self.server = RESTAPI_38
        else:
            self.server = RESTAPI_37

    def ping_server(self, server=RESTAPI_38):
        """ping ensembl

        Accepts:
            server(str): default is 'https://grch37.rest.ensembl.org'

        Returns:
            data(dict): dictionary from json response
        """
        url = "/".join([server, PING_ENDPOINT])
        data = self.send_request(url)
        return data

    def except_on_invalid_response(self, resp):
        """Checks if Ensembl service returned a valid response(status:200->OK), otherwise raise error with informative message"""
        # If service returned error
        if resp.status != 200:
            # raise an exception with a proper message
            raise Exception(
                f"Ensembl Rest API server returned error {str(resp.status)} (it's probably down) and gene info could not be converted. Please try again later."
            )

    def send_request(self, url):
        """Sends the actual request to the server and returns the response

        Accepts:
            url(str): ex. https://grch37.rest.ensembl.org/lookup/id/ENSG00000103591

        Returns:
            data(dict): dictionary from json response
        """
        data = {}
        try:
            request = Request(url, headers=HEADERS)
            response = urlopen(request)
            self.except_on_invalid_response(response)
            content = response.read()
            if content:
                data = json.loads(content)
        except HTTPError as e:
            LOG.info("Request failed for url {0}: Error: {1}\n".format(url, e))
            data = e
        except ValueError as e:
            LOG.info("Request failed for url {0}: Error: {1}\n".format(url, e))
            data = e
        return data
